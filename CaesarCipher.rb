#
# Making a Caesar Cipher Encryption program
# 

def CaesarCipher(text, key)
    alphabets = ('a'..'z').to_a
    cipher = Array.new
    text.split('').each do |letter|
        letter_index = alphabets.index(letter)
        cipher_letter = alphabets[(letter_index + key) % 26]
        cipher.append(cipher_letter)
    end
    ciphered_text = cipher.join('')
    return ciphered_text
end

print "Text to cipher: "
text = gets.chomp()

print "Key: "
key = gets.chomp()

puts CaesarCipher(text.downcase,key.to_i)