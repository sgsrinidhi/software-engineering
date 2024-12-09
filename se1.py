import math
import matplotlib.pyplot as plt
import numpy as np

# Function to solve quadratic equation
def solve_quadratic(a, b, c):
    try:
        discriminant = b**2 - 4*a*c
        
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            return root1, root2
        elif discriminant == 0:
            root = -b / (2*a)
            return root,
        else:
            return "No real solutions"
    except Exception as e:
        return f"Error: {e}"

# Function to plot the quadratic equation and roots
def plot_quadratic(a, b, c, roots):
    # Create an array of x values from -10 to 10 (adjust as needed)
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    
    plt.plot(x, y, label=f'{a}x² + {b}x + {c}', color='blue')
    
    if len(roots) == 1:
        plt.plot(roots[0], 0, 'ro', label=f'Root: {roots[0]}')
    elif len(roots) == 2:
        plt.plot(roots[0], 0, 'ro', label=f'Root 1: {roots[0]}')
        plt.plot(roots[1], 0, 'go', label=f'Root 2: {roots[1]}')
    
    # Adding title and labels
    plt.title(f"Graph of the quadratic equation {a}x² + {b}x + {c}")
    plt.xlabel("x")
    plt.ylabel("y")
    
    # Adding a grid and legend
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.grid(True)
    plt.legend()
    
    # Display the plot
    plt.show()

def main():
    # Step 1: Hard-coded Variables
    a = 1
    b = -3
    c = 2
    print("Hard-coded example:")
    solutions = solve_quadratic(a, b, c)
    print(f"Solutions for a={a}, b={b}, c={c}: {solutions}\n")
    plot_quadratic(a, b, c, solutions)
    
    # Step 2: Keyboard Input
    print("Enter coefficients for the quadratic equation (a, b, c):")
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        solutions = solve_quadratic(a, b, c)
        print(f"Solutions for a={a}, b={b}, c={c}: {solutions}\n")
        plot_quadratic(a, b, c, solutions)
    except ValueError:
        print("Invalid input. Please enter numeric values for a, b, and c.\n")

   

if __name__ == "__main__":
    main()
