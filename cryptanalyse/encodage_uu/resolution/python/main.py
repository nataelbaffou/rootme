
def default_lib(src: str):
    print(bytearray.fromhex(src).decode())

def manual(src: str):
    # First step: Extract the relevant part of the encoded data
    # I'm gonna be laxist and search the lines that start with "begin" and "end" without controlling if they are the good ones
    # And take what's inside as relevant data
    lines = src.split('\n')
    try:
        l_start = [i for i, l in enumerate(lines) if l.startswith("begin")][0]
        l_end = [i for i, l in enumerate(lines) if l.startswith("end")][0]
    except IndexError:
        print("Either the begin or end line is missing")
        exit()

    content = lines[l_start+1:l_end]

    # Second step: Decode it
    final_data = ""
    for l in content:
        curated_line = l.replace("`", " ")[1:] # Take only content
        for i in range(len(curated_line)//4):
            u1, u2, u3, u4 = ord(curated_line[0+i*4])-32, ord(curated_line[1+i*4])-32, \
                             ord(curated_line[2+i*4])-32, ord(curated_line[3+i*4])-32
            v1 = ((u1 << 2) & 255) + (u2 >> 4)
            v2 = ((u2 << 4) & 255) + (u3 >> 2)
            v3 = ((u3 << 6) & 255) + u4

            final_data = final_data + \
                         ("" if v1 == 0 else chr(v1)) + \
                         ("" if v2 == 0 else chr(v2)) + \
                         ("" if v3 == 0 else chr(v3))

    print(final_data)


if __name__ == "__main__":
    src_ = """
_=_
_=_ Part 001 of 001 of file root-me_challenge_uudeview
_=_

begin 644 root-me_challenge_uudeview
B5F5R>2!S:6UP;&4@.RD*4$%34R`](%5,5%)!4TE-4$Q%"@``
`
end
"""
    manual(src_)
    #default_lib(src_)