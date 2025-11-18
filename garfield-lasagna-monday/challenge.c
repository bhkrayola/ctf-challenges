#include <emscripten/emscripten.h>
#include <stdint.h>
#include <stddef.h>

static const uint8_t XOR_KEY = 0x55u;
static const uint8_t obf_input[32] = {
    0x62 ^ XOR_KEY,   // 'b' ^ 0x55 = 0x37
    0x6C ^ XOR_KEY,   // 'l' ^ 0x55 = 0x39
    0x75 ^ XOR_KEY,   // 'u' ^ 0x55 = 0x20
    0x65 ^ XOR_KEY,   // 'e' ^ 0x55 = 0x30
    0x7C ^ XOR_KEY,   // '|' ^ 0x55 = 0x29

    0x74 ^ XOR_KEY,   // 't' ^ 0x55 = 0x21
    0x75 ^ XOR_KEY,   // 'u' ^ 0x55 = 0x20
    0x78 ^ XOR_KEY,   // 'x' ^ 0x55 = 0x2D
    0x65 ^ XOR_KEY,   // 'e' ^ 0x55 = 0x30
    0x64 ^ XOR_KEY,   // 'd' ^ 0x55 = 0x31
    0x6F ^ XOR_KEY,   // 'o' ^ 0x55 = 0x3A
    0x7C ^ XOR_KEY,   // '|' ^ 0x55 = 0x29

    0x64 ^ XOR_KEY,   // 'd' ^ 0x55 = 0x31
    0x61 ^ XOR_KEY,   // 'a' ^ 0x55 = 0x34
    0x6E ^ XOR_KEY,   // 'n' ^ 0x55 = 0x3B
    0x63 ^ XOR_KEY,   // 'c' ^ 0x55 = 0x36
    0x65 ^ XOR_KEY,   // 'e' ^ 0x55 = 0x30
    0x7C ^ XOR_KEY,   // '|' ^ 0x55 = 0x29

    0x63 ^ XOR_KEY,   // 'c' ^ 0x55 = 0x36
    0x68 ^ XOR_KEY,   // 'h' ^ 0x55 = 0x3D
    0x61 ^ XOR_KEY,   // 'a' ^ 0x55 = 0x34
    0x6F ^ XOR_KEY,   // 'o' ^ 0x55 = 0x3A
    0x73 ^ XOR_KEY,   // 's' ^ 0x55 = 0x26
    0x7C ^ XOR_KEY,   // '|' ^ 0x55 = 0x29

    0x70 ^ XOR_KEY,   // 'p' ^ 0x55 = 0x25
    0x61 ^ XOR_KEY,   // 'a' ^ 0x55 = 0x34
    0x6E ^ XOR_KEY,   // 'n' ^ 0x55 = 0x3B
    0x63 ^ XOR_KEY,   // 'c' ^ 0x55 = 0x36
    0x61 ^ XOR_KEY,   // 'a' ^ 0x55 = 0x34
    0x6B ^ XOR_KEY,   // 'k' ^ 0x55 = 0x3E
    0x65 ^ XOR_KEY,   // 'e' ^ 0x55 = 0x30
    0x73 ^ XOR_KEY    // 's' ^ 0x55 = 0x26
};

EMSCRIPTEN_KEEPALIVE
int check(const char *inp) {
    for (size_t i = 0; i < 32; i++) {
        uint8_t b = (uint8_t)inp[i];
        if (((uint8_t)(b ^ XOR_KEY)) != obf_input[i]) {
            return 0;
        }
    }
    if (inp[32] != '\0') {
        return 0;
    }
    return 1;
}


static const uint8_t enc_flag[24] = {
    0xAC, 0xBA, 0x8F, 0xAB, 0xAE, 0x07, 0x29, 0x5C,
    0x9E, 0x3A, 0x1D, 0xF2, 0xB1, 0xE7, 0xB5, 0xD4,
    0xB4, 0x9E, 0x4B, 0xCC, 0x26, 0xB0, 0xCA, 0x6A
};
static const size_t enc_flag_len = sizeof(enc_flag) / sizeof(enc_flag[0]);

#define LCG_A 1103515245u
#define LCG_C 12345u

static char flagbuf[32];

EMSCRIPTEN_KEEPALIVE
const char* get_flag() {
    uint32_t state = 0x13371337u;
    for (size_t i = 0; i < enc_flag_len; i++) {
        state = (uint32_t)(state * LCG_A + LCG_C);
        uint8_t key = (uint8_t)((state >> 16) & 0xFFu);
        flagbuf[i] = (char)(enc_flag[i] ^ key);
    }
    flagbuf[enc_flag_len] = '\0';
    return (const char*)flagbuf;
}
