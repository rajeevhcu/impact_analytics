def sort_list_by_xz(x1x2h_list):
    """sort list by x1 asc and h by desc"""
    x1x2h_list = sorted(x1x2h_list, key=lambda element: element[0])
    for i in range(len(x1x2h_list)):
        p = 0
        for j in range(i + 1, len(x1x2h_list)):
            if x1x2h_list[i][0] == x1x2h_list[j][0]:
                p = j
                continue
            else:
                x1x2h_list[i:j] = sorted(x1x2h_list[i:j], key=lambda ele: ele[2], reverse=True)
                break
        else:
            if p:
                x1x2h_list[i:p + 1] = sorted(x1x2h_list[i:p + 1], key=lambda ele: ele[2], reverse=True)
    return x1x2h_list


def arrange_cardboard(x1x2h_list):
    sorted_x1x2h = sort_list_by_xz(x1x2h_list)
    final_cardboard = []
    for i in range(len(sorted_x1x2h) - 1):
        if len(final_cardboard) == 0:
            final_cardboard.append((sorted_x1x2h[i][0], sorted_x1x2h[i][2]))
        if sorted_x1x2h[i + 1][0] < sorted_x1x2h[i][1] < sorted_x1x2h[i + 1][1]:
            if sorted_x1x2h[i][2] > sorted_x1x2h[i + 1][2]:
                final_cardboard.append((sorted_x1x2h[i][1], sorted_x1x2h[i + 1][2]))
            else:
                final_cardboard.append((sorted_x1x2h[i + 1][0], sorted_x1x2h[i + 1][2]))
        elif sorted_x1x2h[i][1] < sorted_x1x2h[i + 1][0]:
            final_cardboard.append((sorted_x1x2h[i][1], 0))
            final_cardboard.append((sorted_x1x2h[i + 1][0], sorted_x1x2h[i + 1][2]))
        elif sorted_x1x2h[i + 1][0] > sorted_x1x2h[i][0] and sorted_x1x2h[i + 1][1] < sorted_x1x2h[i][1] and \
                sorted_x1x2h[i + 1][
                    2] > sorted_x1x2h[i][2]:
            final_cardboard.append((sorted_x1x2h[i + 1][0], sorted_x1x2h[i + 1][2]))
            final_cardboard.append((sorted_x1x2h[i + 1][1], sorted_x1x2h[i][2]))
        if i == len(sorted_x1x2h) - 2:
            if sorted_x1x2h[i + 1][0] < sorted_x1x2h[i][1] < sorted_x1x2h[i + 1][1]:
                final_cardboard.append((sorted_x1x2h[i + 1][1], 0))
            else:
                final_cardboard.append((sorted_x1x2h[i][1], 0))
    return final_cardboard


if __name__ == '__main__':
    unsorted = [(1, 5, 10), (4, 6, 8), (10, 15, 10), (11, 12, 8)]
    print(arrange_cardboard(unsorted))
