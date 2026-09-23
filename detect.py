alice_key = [1,0,1,1,0,1,0,1]
bob_key = [1,0,0,1,0,1,1,1]
errors = 0
for i in range(len(alice_key)):
    if alice_key[i] != bob_key[i]:
        errors += 1
print("Alice Key :", alice_key)
print("Bob Key :", bob_key)
print("Number of Errors:", errors)
error_rate = (errors / len(alice_key)) * 100
print("Error Rate :", error_rate,"%")

if error_rate > 10:
    print("Warning : Eavesdropper Detected!")
else:
    print("Secure Communication")