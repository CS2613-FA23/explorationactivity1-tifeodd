import matplotlib.pyplot as plt

def create_sales_report_chart():
    
    products = ['Product A', 'Product B', 'Product C', 'Product D']
    sales = [12000, 18000, 15000, 20000]

   
    colors = ['royalblue', 'forestgreen', 'gold', 'tomato']

  
    plt.bar(products, sales, color=colors)

   
    plt.xlabel('Products')
    plt.ylabel('Sales Amount (in USD)')
    plt.title('Product Sales Report')

   
    for i, value in enumerate(sales):
        plt.text(i, value, str(value), ha='center', va='bottom')

  
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.ylim(0, max(sales) + 2000)

   
    plt.show()

if __name__ == "__main__":
    create_sales_report_chart()
