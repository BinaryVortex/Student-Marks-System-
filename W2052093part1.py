#Importing packages/modules for the project.
import graphics as gr

#Creating and Initializing for progression outcomes and variables.
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0

#Creating a list for progress data.
progress_data = []

#Creating of a function to write the data to a text file.
def write_to_file(filename, data):
    with open(filename, "w") as file:
        for item in data:
            file.write(f"{item}\n")

#Getting the progession outcome 
def progression_outcome(pass_credits, defer_credits, fail_credits):
    if pass_credits == 120 and defer_credits == 0 and fail_credits == 0:
        return "Progress"
    elif pass_credits == 100 and defer_credits == 20 and fail_credits == 0 or pass_credits == 100 and defer_credits == 0 and fail_credits == 20:
        return "Progress (module trailer)"
    elif fail_credits >= 80:
        return "Exclude"
    else:
        return "Do not progress - module retriever"
    
# Function to display the histogram
def display_histogram(progress_count, trailer_count, retriever_count, exclude_count):
    win = gr.GraphWin("Progression Outcomes Histogram", 800, 300)
    win.setBackground("white")

    progress = gr.Rectangle(gr.Point(50, 250), gr.Point(150, 250 - progress_count))
    trailer = gr.Rectangle(gr.Point(200, 250), gr.Point(300, 250 - trailer_count))
    retriever = gr.Rectangle(gr.Point(350, 250), gr.Point(450, 250 - retriever_count))
    exclude = gr.Rectangle(gr.Point(500, 250), gr.Point(600, 250 - exclude_count))

    progress_label = gr.Text(gr.Point(100, 270), f"Progress: {progress_count}")
    trailer_label = gr.Text(gr.Point(250, 270), f"Trailing: {trailer_count}")
    retriever_label = gr.Text(gr.Point(400, 270), f"Module Retriever: {retriever_count}")
    exclude_label = gr.Text(gr.Point(550, 270), f"Exclude: {exclude_count}")

    progress.setFill("Light Green")
    trailer.setFill("Dark Sea Green")
    retriever.setFill("Yellow Green")
    exclude.setFill("Dark Salmon")

    progress.draw(win)
    trailer.draw(win)
    retriever.draw(win)
    exclude.draw(win)

    progress_label.draw(win)
    trailer_label.draw(win)
    retriever_label.draw(win)
    exclude_label.draw(win)

    # Calculate and display the total number of outcomes
    total_outcomes = progress_count + trailer_count + retriever_count + exclude_count
    total_label = gr.Text(gr.Point(700, 270), f"Total Outcomes: {total_outcomes}")
    total_label.draw(win)

    win.getMouse()
    win.close()

#Creating the main program loop using a while True loop.
while True:
    try:
        pass_credits = int(input("Enter your pass credits: "))
        defer_credits = int(input("Enter your defer credits: "))
        fail_credits = int(input("Enter your Fail credits: "))
        

        #Creaation of a User_List and entering variables inside
        UserInput_list = [pass_credits, defer_credits, fail_credits]

        #Checking the user input if the remainder is zero
        if pass_credits % 20 == 0 and defer_credits % 20 == 0 and fail_credits % 20 == 0:
            total_credits = pass_credits + defer_credits + fail_credits

            #if total credits is equal to 120 the progession outcome will be displayed.
            if total_credits == 120:
                outcome = progression_outcome(pass_credits, defer_credits, fail_credits)
                print(outcome)

                #Update counts for the histogram
                if outcome == "Progress":
                    progress_count += 1
                elif outcome == "Progress (module trailer)":
                    trailer_count += 1
                elif outcome == "Do not progress - module retriever":
                    retriever_count += 1
                elif outcome == "Exclude":
                    exclude_count += 1

                #Appending the inputs to progress data list.
                progress_data.append((outcome, *UserInput_list))

                #Asking user if he wants to enter another set of data.
                while True:
                    choice = input("Would you like to enter another set of data? Enter 'y' for yes or 'q' to quit: ")

                    #If choice is y.
                    if choice.lower() == 'y':
                        break

                    #If choice is q.
                    elif choice.lower() == 'q':
                        break

                    #If another value other than y or q is entered.
                    else:
                        print("Invalid input. Please enter 'y' or 'q'.")
                
                #Breaking the loop if user input is q.
                if choice.lower() == 'q':
                    break

            #In case the total credits is not equal to 120.
            else:
                print("Total incorrect")

    #Case of ValueError
    except ValueError:
        print("Integer is required")
        

# Display the histogram and results
display_histogram(progress_count, trailer_count, retriever_count, exclude_count)

#Printing part 2.
print("Part 2:")

#Getting values from data point list and printing values.
for data_point in progress_data:
    print(f"{data_point[0]} - {data_point[1]}, {data_point[2]}, {data_point[3]}")

#Calling the write to file function.
write_to_file("progress_report.txt", progress_data)

#Printing the results are saved.
print("Results saved to progress_report.txt")

