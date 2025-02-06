def main():
    # Read the starting size of Dusa
    dusa_size = int(input())
    
    # Read the subsequent Yobis' sizes
    while True:
        yobi_size = int(input())
        
        # If Dusa encounters a Yobi that is the same size or larger, it runs away
        if yobi_size >= dusa_size:
            print(dusa_size)
            break
        
        # Otherwise, Dusa eats the Yobi and grows in size
        dusa_size += yobi_size

if __name__ == "__main__":
    main()
