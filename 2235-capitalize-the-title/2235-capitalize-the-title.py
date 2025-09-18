class Solution:
    def capitalizeTitle(self, title: str) -> str:
        arr = title.split(" ")
        for index in range(len(arr)):
            if len(arr[index]) > 2:
                arr[index] = arr[index].capitalize()
            else:
                arr[index] = arr[index].lower()
        return " ".join(arr)
        