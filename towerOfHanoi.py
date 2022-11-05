def toh(n, from_a, to_c, ax):
    if n == 1:
        return print("Move Disk 1 from ", from_a, " to ", to_c)
    else:
        toh(n-1, from_a, ax, to_c)
        print("Move Disk", n, "from ", from_a, " to ", to_c)
        toh(n-1, ax, to_c, from_a)
        
n = int(input('Enter Number of Disks :'))
toh(n, "A", 'C', 'B')
    
