var wpop = document.getElementById("popid").textContent;
function isNumber(value) {
    return typeof value === "number";
  }
  const userInteractionEvents = [
    // coming soon other user interaction
    // "click",
    // "dblclick",
    // "mousedown",
    // "keydown",
    // "keyup",
    // "load",
    // "keypress",
    // "input",
    // "change",
    // "submit",
    // "drag",
    // "drop",
    "mouseup",
    // "touchstart",
    // "touchend",
    // "touchmove",
    // "pointerdown",
    // "pointerup",
    // "pointermove",
    // "contextmenu",
  ];

  function mouse_down() {
    var category = document.getElementById("headache-category").value;

    if (userInteractionEvents.includes(category)) {
      console.log(`Category is valid: ${category}`);
    } else {
      return alert("I don't know that category");
     
    }

    var filtered_num = document.getElementById("number-selector").value;
    var filtered_nums = document.getElementById("number-happy").value;
    var filtered_num = DOMPurify.sanitize(filtered_num);
    var filtered_nums = DOMPurify.sanitize(filtered_nums);
    if (filtered_num > 1000) {
      return alert("sorry you are not a headache master");
    }
    var filtered_num = filtered_num - filtered_nums;
    if (isNumber(filtered_num) == false) {
      return alert("sorry you are not a hacker master");
    }
    console.log(filtered_num);
    var b = window.open(wpop, "poppin_a_headache");
    var filtered_headache = document.getElementById("your-headache").value;
    if (filtered_headache.includes("(")) {
      return alert(
        "hehe, incase you got cve from dompurify, for secure only. just ignore it"
      );
    }
    if (filtered_headache.includes(")")) {
      return alert(
        "hehe, incase you got cve from dompurify, for secure only. just ignore it"
      );
    }
    var filtered_headache = DOMPurify.sanitize(filtered_headache);

    if (
        wpop.includes("http://localhost") ||
      !wpop.includes("/")
    ) {
      b.document.write(`
<title>Headache report</title>
<h1>Yep, it was your problem, so your headache</h1>
<p id="trigger-headache">${filtered_headache}</p>
<p id="headache-num">${filtered_num}</p>
<script>
  function up_coming_features() {
    alert('custom user interaction is coming-soon features');
  };
  var w = null;
  window.addEventListener('${category}', function() {
  
    if (w) return;
    w = window.open('${wpop}', 'trigger_me', 'resizeable=1,menubar=0,status=1');
    w.document.write("${filtered_headache}");
  });
  window.go = function() {
    return document.getElementById("trigger-headache").textContent; 
  };
  if (document.getElementById("headache-num").textContent > 1000) {
    console.info("you so happy already? with your ${filtered_headache} happyness right?. so you dont need to worry about it");
  } else {
    console.log("you are not a headache master") 
  }
  

<\/script>
`);
    }

    function checkGoFunction() {
      try {
        if (typeof b.go === "function") {
          b.go();
          alert("fixing headache now : ", b.go());
          b.close();
        } else {
          setTimeout(checkGoFunction, 100);
        }
      } catch (e) {
        console.error("Error:", e);
      }
    }
    checkGoFunction();
  }
  (function () {
    if (!wpop.includes(":") && !wpop.startsWith("http")) {
      alert(
        `wpop is not valid, please use a valid domain  by setting the ?pop=site`
      );
      location.href = wpop;
    }

    var w = null;
    var winName = "Headache";
    var winParams =
      "status=1,menubar=0,toolbar=0,height=1152,width=2048,top=0,location=0,scrollbars=0,resizable=1,left=0";

    var link = document.getElementById("th");
    // link.addEventListener(category, function () {
    //   if (w) return;
    //   w = window.open("{{wpop}}", winName, winParams);
    //   w.resizeTo(1, 0);
    //   w.moveTo(9e5, 9e5);
    // });
  })();