def movetower(height,fp,tp,wp):
    if height>=1:
        movetower(height-1, fp, wp, tp)
        movefromto(fp,tp)
        movetower(height - 1, wp, tp, fp)

def movefromto(fp,tp):
    print("Moving ring from "+fp +" to "+tp)


def main():
    movetower(4, "A", "B", "C")

main()