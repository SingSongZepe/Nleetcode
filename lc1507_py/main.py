


class Solution:
    def reformatDate(self, date: str) -> str:

        month = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12"
        }

        d, m, y = date.split()
        d = ''.join(filter(str.isdigit, d))

        return y + '-' + month[m] + '-' + (d if len(d) == 2 else '0' + d)

class Solution1:
    def reformatDate(self, date: str) -> str:

        months = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12"
        }

        d, m, y = date.split()
        d = d[:-2]               # drop the last two characters

        return y + "-" + months[m] + "-" + (d if len(d) == 2 else "0" + d)




def main():
    print('Hello World')

if __name__ == '__main__':
    main()