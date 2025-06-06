const { default: axios } = require("axios");
const { imageToWebp, writeExifImg, videoToWebp, writeExifVid } = require("../../utils/stickerMaker");
const validateUrl = require("../../utils/validate-url.js");
const exp = require('../../utils/exp.js');

module.exports = {
    name : "sticker",
    description : "Sticker Maker",
    cmd : ['sticker', 's', 'stiker'],
    menu : {
        label : 'tools',
    },
    run : async({ m, sock }) => {
        let url = validateUrl(m.body.arg) ? m.body.arg : false
        let image;
        if(!['imageMessage', 'stickerMessage', 'videoMessage'].includes(m.quoted?.mtype || m.mtype) && !url) return m._reply(m.lang(msg).ex);
        m._react(m.key, '🧋')
        if(url) {
            try {
                image = await axios.get(url, { responseType: 'arraybuffer' })
            }catch(error) { return m._reply(m.lang(msg).invalidUrl) }
            if(!['video', 'image'].includes(image.headers.get('content-type').split('/')[0])) return m._reply(m.lang(msg).req)
            image = {
                buffer : image.data,
                ext : image.headers.get('content-type').split('/')[1],
                mtype : image.headers.get('content-type').split('/')[0]+'Message'
            }
        } else {
            image = m.quoted ? await m.quoted.download() : await m.download();
        }

        if(image.mtype === 'imageMessage' || image.mtype === 'stickerMessage') {
            let sticker = await imageToWebp(image.buffer)
            sticker = await writeExifImg(sticker, { packname : m.db.bot.exif.pack || '-', author : m.db.bot.exif.author || '-' })
            exp.add(m.sender, exp.random(1, 5))
            await m._sendMessage(m.chat, { sticker : sticker }, { quoted: m })
            m._react(m.key, '✅')
        } else if(image.mtype === 'videoMessage') {
            let sticker = await videoToWebp(image.buffer)
            sticker = await writeExifVid(sticker, { packname : m.db.bot.exif.pack || '-', author : m.db.bot.exif.author || '-' })
            exp.add(m.sender, exp.random(1, 5))
            await m._sendMessage(m.chat, { sticker : sticker }, { quoted: m })
            m._react(m.key, '✅')
        } else {
            m._react(m.key, '❌')
            m._reply(m.lang(msg).req)
        }
    }
}

const msg = {
    id: {
        ex: '*Penggunaan*:\n- Balas gambar atau sticker dengan caption `{prefix}sticker`\n- Kirim gambar atau video dengan caption `{prefix}sticker`\n- {prefix}sticker <url>\n\n*Keterangan*:*\n- *<url>*: URL berisi gambar atau video.',
        req: 'Format yang diperbolehkan: `gambar`, `stiker`, atau `video`.',
        invalidUrl: 'URL tidak valid.'
    },
    en: {
        ex: '*Usage:*\n- Reply to an image or sticker with the caption `{prefix}sticker`\n- Send an image or video with the caption `{prefix}sticker`\n- {prefix}sticker <url>\n\n*Description:*\n- *<url>*: URL contains image or video.',
        req: 'Must be in the format: image, sticker, or video.',
        invalidUrl: 'URL is invalid.'
    }
}
