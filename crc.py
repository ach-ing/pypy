import random
import copy

#crc32(castagnoli) polynom
polynom = 0x1EDC6F41

#input polynom into a list
polynom_list = [int(x) for x in bin(polynom)[2:]]

#func generating k-len message
def genRandMess(k):
    message = [random.randint(0,1) for i in range(k)]
    
    return message


#func for calculating CRC32(castagnoli)
def crc32(message, poly):
    
    
    registry = [0 for i in range (len(poly)-1)]
    
    message.extend(registry)
    
    while(len(message) != 0):
        firstRegBit = registry[0]
        
        #throw out the first bit in registry - bit shifting
        for i in range(len(registry) - 1):
            registry[i] = registry[i+1]
        
        #put first message bit in the end of the registry
        registry[len(registry) - 1] = message[0]
        #removing that bit from the message list
        message.remove(message[0])
        
        #if the firts registry bit is 1 - means we need to XOR
        if firstRegBit == 1:
            for i in range(len(registry)):
                registry[i] = (registry[i] + poly[i+1]) % 2

return registry

# print('Len of the message:')
k = int(input())

mess2 = genRandMess(k)
mess = copy.deepcopy(mess2)
print("Our message:", mess2,'its len:', len(mess2))

Crc_res = crc32(mess2, polynom_list)

print("Res of CRC - CHECKSUM:", Crc_res, "it's len:", len(crc_res1))
mess.extend(Crc_res)

print("Our extended message:", mess, "it's len:", len(mess))

print('CRC check')

result = crc32(mess, polynom_list)

print(result)


