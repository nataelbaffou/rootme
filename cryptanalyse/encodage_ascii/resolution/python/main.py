
def default_lib(src: str):
    print(bytearray.fromhex(src).decode())

def manual(src: str):
    dst_chr = []
    for i in range(0, len(src), 2):
        dst_chr.append(chr(int(src[i:i+2], 16)))
    print("".join(dst_chr))



if __name__ == "__main__":
    src_ = "436563692065737420756E6520706872617365207061722064656661757420706F75722063652070726F6A65742E204E6174"
    manual(src_)
    default_lib(src_)