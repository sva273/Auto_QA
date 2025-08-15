

class Tree:
    def garland_length(self, arr):
        length = 0

        for i in range(len(arr) - 1):
            distance = abs(arr[i + 1] - arr[i])
            length += distance

        return length

if __name__ == "__main__":
    tree = Tree()
    bulbs_sequence = [1, 2, 3, 4, 5]
    print("Length:", tree.garland_length(bulbs_sequence))