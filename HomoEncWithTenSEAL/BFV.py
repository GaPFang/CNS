import tenseal as ts

# === STEP 1: Load the public key ===
with open("public.key", "rb") as f:
    public_context = ts.context_from(f.read())

# === STEP 2: Load the provided ciphertext from TA ===
with open("B11901003.tenseal", "rb") as f:   # change to your filename
    ta_cipher = ts.bfv_vector_from(public_context, f.read())

# === STEP 3: Prepare your student ID ===
student_id = 11901003          # change this to YOUR full student ID
last_five_digits = student_id % 100000  # get the last 5 digits
print("Last five digits:", last_five_digits)

# === STEP 4: Encrypt your number ===
my_cipher = ts.bfv_vector(public_context, [last_five_digits])

# === STEP 5: Perform homomorphic addition ===
result_cipher = my_cipher + ta_cipher

# === STEP 6: Save the resulting ciphertext ===
output_filename = f"B{student_id}_enc_result.tenseal"
with open(output_filename, "wb") as f:
    f.write(result_cipher.serialize())

print("✅ Encrypted result saved as:", output_filename)
