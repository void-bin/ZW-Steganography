ZWSP = u'\u200b'

def hide_msg_in_text(text, msg):
    hidden_char_map = {True: ZWSP, False: u'\u200c'}
    binary_msg = ''.join(format(ord(c), '08b') for c in msg)
    hidden_msg = ''.join(hidden_char_map[b == '1'] for b in binary_msg)
    return text + hidden_msg

def extract_msg_from_text(text):
    hidden_char_map_inverse = {ZWSP: '1', u'\u200c': '0'}
    binary_msg = ''.join(hidden_char_map_inverse[c] for c in text if c in hidden_char_map_inverse)
    msg = ''.join(chr(int(binary_msg[i:i+8], 2)) for i in range(0, len(binary_msg), 8))
    return msg

def main():
    original_text = "This is the cover text."
    secret_msg = "Hidden message"

    hidden_content = hide_msg_in_text(original_text, secret_msg)
    extracted_msg = extract_msg_from_text(hidden_content)

    print("Original Text:           ", original_text)
    print("Text with Hidden Message:", hidden_content)
    print("Extracted Secret Message:", extracted_msg)

if __name__ == "__main__":
	main()
