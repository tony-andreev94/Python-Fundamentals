# Create a program that calculates what percentage you can cover of a 6-sided gift box (all sides are equal and square).
# First, you will receive the size of a side. Also, you will receive the sheets of paper you have.
# Last, you will receive how much area covers a single sheet of paper.
# First, you need to calculate the area of the gift box. Then you have to calculate how much area you can cover
# with the paper available. Keep in mind that every third sheet covers only 25% of the usual area.
# You have to calculate what percentage of the gift box you’ve covered. Percentage can exceed 100%!
# In the end, print the percentage of the area covered, formatted to the 2nd decimal place, in the following format:
# "You can cover {percentage}% of the box."

# Take input
box_side = float(input())
paper_sheets = int(input())
paper_area = float(input())

total_box_area = (box_side ** 2) * 6
third_sheets = paper_sheets // 3
total_covered_area = (paper_sheets - third_sheets) * paper_area + (third_sheets * 0.25 * paper_area)
covered_percentage = total_covered_area / total_box_area * 100

# Print result
print(f"You can cover {covered_percentage:.2f}% of the box.")


