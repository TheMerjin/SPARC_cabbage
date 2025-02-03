import numpy as np
import matplotlib.pyplot as plt
import random

def simulate_cabbage_business(days=100, trials=1000, cancellation_prob=0.2, strategy='buffer'):
    profits = []
    
    for _ in range(trials):
        money = 0
        inventory = 0
        pending_orders = []  # Tracks open orders with deadlines
        pending_delveries = []
        
        for day in range(days):
            if random.random()> 0.2:
                for deliveries, ord_amt in pending_delveries:
                    if deliveries == day+1:
                        pending_delveries.remove((deliveries, ord_amt))
            



            # 1. Accept order and promise delivery in 3 days
            pending_orders.append(day + 3)
            if strategy == 'buffer':
                order_amount = 2  # The situation where ordering extra to mitigate risk
            else:
                order_amount = 1  # ordering enough
            money -= 1*order_amount  # Cost of ordering cabbage
            
            # 2. Place order with the farmer
            pending_delveries.append((day+2, order_amount))

            
                        
                                
           
            for deliveries, ord_amt in pending_delveries:
                if deliveries == day:
                    inventory += ord_amt
                    pending_delveries.remove((deliveries, ord_amt))
            
            # 4. Deliver orders if inventory allows
            left_orders = [deadline for deadline in pending_orders if deadline < day]
            pending_orders = [deadline for deadline in pending_orders if deadline >= day]

            while inventory > 0 and pending_orders:
                inventory -= 1
                pending_orders.pop(0)
                money += 4 
            
            
            if len(pending_orders) > 0:
                failed_orders = len(pending_orders)
                money -= 5 * failed_orders  
                pending_orders = []
            
            
            pending_orders = left_orders
            
            inventory = 0
        
        profits.append(money)
    
    return np.mean(profits)
def simulate_cabbage_business2(days=100, trials=1000, cancellation_prob=0.2, strategy='buffer'):
    profits = []
    
    for _ in range(trials):
        money = 0
        inventory = 0
        pending_orders = []  
        pending_delveries = []
        
        for day in range(days):
           
            pending_orders.append(day + 3)
            if strategy == 'buffer':
                order_amount = 2  
            else:
                order_amount = 1  
            money -= 1*order_amount  
            
            pending_delveries.append((day+2, order_amount))

            if random.random()> 0.2:
                for deliveries, ord_amt in pending_delveries:
                    if deliveries == day+1:
                        pending_delveries.remove((deliveries, ord_amt))
                        
                                
            
            for deliveries, ord_amt in pending_delveries:
                if deliveries == day:
                    inventory += ord_amt
                    pending_delveries.remove((deliveries, ord_amt))
            
            
            left_orders = [deadline for deadline in pending_orders if deadline < day]
            pending_orders = [deadline for deadline in pending_orders if deadline >= day]

            while inventory > 0 and pending_orders:
                inventory -= 1
                pending_orders.pop(0)
                money += 4  
            
            
            
            if len(pending_orders) > 0:
                failed_orders = len(pending_orders)
                money -= 5 * failed_orders  
                pending_orders = []
            pending_orders = left_orders
            
            inventory = 0
        
        profits.append(money)
    
    return np.mean(profits)


# Run simulation for different cancellation probabilities
cancellation_probs = np.linspace(0, 1, 11)
buffer_profits = [simulate_cabbage_business(cancellation_prob=p, strategy='buffer') for p in cancellation_probs]
jit_profits = [simulate_cabbage_business(cancellation_prob=p, strategy='jit') for p in cancellation_probs]
buffer_profits_profits_with_cancelling = [simulate_cabbage_business2(cancellation_prob=p, strategy='buffer') for p in cancellation_probs]
jit_profits_with_cancelling = [simulate_cabbage_business2(cancellation_prob=p, strategy='jit') for p in cancellation_probs]

# Plot results
plt.plot(cancellation_probs, buffer_profits, label='Buffer Strat')
plt.plot(cancellation_probs, jit_profits, label='Just-in-Time Strat')
plt.plot(cancellation_probs, buffer_profits_profits_with_cancelling, label='Buffer Strat with cancelling')
plt.plot(cancellation_probs, jit_profits_with_cancelling, label='Just-in-Time Strat_with_cancelling')
plt.xlabel('Supplier Cancellation Probability')
plt.ylabel('Average Profit over 100 Days')
plt.legend()
plt.title('Monte Carlo Simulation of Cabbage Business')
plt.show()
