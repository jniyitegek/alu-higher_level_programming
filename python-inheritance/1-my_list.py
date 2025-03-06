class MyList(list):
    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))

# Example usage
if __name__ == "__main__":
    my_list = MyList([3, 1, 4, 1, 5, 9, 2, 6])
    my_list.print_sorted()  # Output: [1, 1, 2, 3, 4, 5, 6, 9]

    # Writing test output to tests/1-my_list.txt
    with open("tests/1-my_list.txt", "w") as test_file:
        test_file.write(str(sorted(my_list)) + "\n")

