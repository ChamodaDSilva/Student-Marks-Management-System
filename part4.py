
repeat = 'y' #to run first time of repeating option


progress_count = 0
trailer_count = 0#to get counts of each marks catogories
retriever_count = 0
excluded_count = 0

print('--------------------------------------')
print('Staff Version with Histogram\n')


# method for check input is a integer and in the range
def mark_check(v):
    '''to check the input marks are in range and a integer'''
    while True:
        try:
            mark = int(input(f'Enter your total {v.upper()} credits: '))
            while mark not in range(0,121,20):
                print('Out of range.')
                mark = int(input(f'Enter your total {v.upper()} credits: '))
            break
        except ValueError:
            print('Integer required.')
    return mark

#Histogram printing
def histogram():
    '''to print the historigm'''
    print('-------------------------------------------')
    print('Progress | Trailing | Retriever | Excluded ')#header of the table
    for x in range(max(progress_count, trailer_count, retriever_count, excluded_count)):#this max get the maximum of the given table then it gets as the range
        print("  {0}           {1}           {2}           {3}".format(
            '*' if x < progress_count else ' ',
            '*' if x < trailer_count else ' ',#if a count is higer than x then print a * else print a space
            '*' if x < retriever_count else ' ',
            '*' if x < excluded_count else ' '
        ))

    all_counts = progress_count + trailer_count + retriever_count + excluded_count
    print(all_counts,'outcomes in total')
    print('-------------------------------------------')


while repeat == 'y' or repeat == 'yes':
    total = 0#to run the total while loop first time
    while total!=120:
        pass_mark = mark_check('pass')

        defer_mark = mark_check('defer')

        fail_mark = mark_check('fail')

        total = pass_mark + defer_mark + fail_mark
        if total != 120:
            print('Total incorrect.\n')

        # Display Progression Outcome


    if pass_mark == 120:
        print("Progress")
        progress_count += 1

    elif pass_mark == 100:
        print("Progress (module trailer)")
        trailer_count += 1

    elif fail_mark < 80:
        print("Do not progress - module retriever")
        retriever_count += 1

    elif fail_mark >= 80:
        print("Exclude")
        excluded_count += 1

    # repeating option
    print('\nWould you like to enter another set of data?')
    repeat = input("Enter 'y' for yes or 'q' to quit and view results: ")
    repeat = repeat.lower()#support for any cases
    while repeat != 'y' and repeat != 'yes' and repeat != 'quit' and repeat != 'q':
        print('Enter a correct option.\n')
        repeat = input("Enter 'y' for yes or 'q' to quit and view results: ")
        repeat = repeat.lower()
    print()

histogram()
