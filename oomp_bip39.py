from pathlib import Path
import hashlib


_BIP39_WORDS = None


def _load_bip39_words():
    global _BIP39_WORDS

    if _BIP39_WORDS is None:
        wordlist_path = Path(__file__).resolve().parent / "source" / "bip_39_wordlist.txt"
        with wordlist_path.open("r", encoding="utf-8") as handle:
            _BIP39_WORDS = [line.strip() for line in handle if line.strip()]

        if len(_BIP39_WORDS) < 256:
            raise ValueError("BIP-39 word list must contain at least 256 words")

    return _BIP39_WORDS


def _hex_to_words(hex_string):
    words = _load_bip39_words()

    if len(hex_string) % 2 != 0:
        raise ValueError("Hex string must have an even number of characters")

    entropy = bytes.fromhex(hex_string)
    entropy_length = len(entropy) * 8

    if entropy_length not in [128, 160, 192, 224, 256]:
        raise ValueError("BIP-39 entropy must be 128, 160, 192, 224, or 256 bits")

    checksum_length = entropy_length // 32
    entropy_bits = "".join(f"{byte:08b}" for byte in entropy)
    checksum_bits = "".join(f"{byte:08b}" for byte in hashlib.sha256(entropy).digest())[:checksum_length]
    combined_bits = entropy_bits + checksum_bits

    return [words[int(combined_bits[index:index + 11], 2)] for index in range(0, len(combined_bits), 11)]


def _build_variants(prefix, words):
    return {
        f"{prefix}_array": words,
        f"{prefix}_space": " ".join(words),
        f"{prefix}_no_space": "".join(words),
        f"{prefix}_underscore": "_".join(words),
    }


def get_bip39_variants(md5_value):
    words = _hex_to_words(md5_value)

    variants = {}
    variants.update(_build_variants("bip_39_full", words))
    variants.update(_build_variants("bip_39_2_word", words[:2]))
    variants.update(_build_variants("bip_39_3_word", words[:3]))
    return variants
