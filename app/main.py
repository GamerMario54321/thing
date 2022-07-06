from hal import hal_rfid_reader as NFC

def main():
    while (true):
        thing = NFC.init()
        print(thing)




def check_NFC_tags():
    while(true):
        thing = NFC.init()
        print(thing)


if __name__ == "__main__":
    main()