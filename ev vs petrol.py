import matplotlib.pyplot as plt

years=6
annual_km=10000
ev_price=14000
petrol_price=10000

ev_consumption=25   # kWh / 100 km
petrol_consumption=6  # L / 100 km
kwh_price=0.09
fuel_price=1.5
fuel_inflation=0.01
investment_return=0.08

sale_price_ev=0.6 * ev_price
sale_price_petrol=0.8 * petrol_price

# godišnja potrošnja
ev_energy_per_year = (annual_km / 100) * ev_consumption
petrol_fuel_per_year = (annual_km / 100) * petrol_consumption

# godišnji troškovi kroz vreme
ev_total_energy_cost = 0
petrol_total_fuel_cost = 0
fuel_price_now = fuel_price
investment = ev_price - petrol_price
invested_value = ev_price - petrol_price

# tracking lists (one point per year)
ev_costs = []
petrol_costs = []
investment_values = []
fuel_prices = []

for year in range(0, years + 1):
    ev_total_energy_cost += ev_energy_per_year * kwh_price
    petrol_total_fuel_cost += petrol_fuel_per_year * fuel_price_now
    invested_value -= petrol_fuel_per_year * fuel_price_now  # oduzimamo troškove goriva iz investicije
    if invested_value > 0:
        invested_value *= 1 + investment_return  # investicija raste svake godine
    fuel_price_now *= (1 + fuel_inflation)  # benzin poskupljuje svake godine

    # save values for plotting
    ev_costs.append(ev_total_energy_cost)
    petrol_costs.append(petrol_total_fuel_cost)
    investment_values.append(invested_value)
    fuel_prices.append(fuel_price_now)

# ukupni troškovi auta
ev_total = ev_price + ev_total_energy_cost - sale_price_ev
petrol_total_net = (invested_value -investment) - petrol_price + sale_price_petrol
petrol_total = petrol_price + petrol_total_fuel_cost - sale_price_petrol

print(f"EV ukupno plaćeno: {ev_total:,.2f} €")
print(f"Petrol ukupno plaćeno: {petrol_total:,.2f} €")
print(f"Investicija vredna posle {years} god: {invested_value:,.2f} €")
print(f"Neto efekat (petrol + investicija): {petrol_total_net:,.2f} €")

if petrol_total_net > -ev_total:
    print("\n→ Benzinski + investiranje isplativije.")
else:
    print("\n→ EV isplativiji.")

# kreiranje figure sa 3 subplot-a u jednom redu
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# 1. linijski graf za investment
axs[0].plot(investment_values, marker='o')
axs[0].set_title("Investment Value")
axs[0].grid(True)

# 2. linijski graf za fuel price
axs[1].plot(fuel_prices, marker='H', color='orange')
axs[1].set_title("Fuel Price")
axs[1].grid(True)

# 3. bar chart za cene auta
labels = ['Petrol', 'EV']
values = [petrol_price, ev_price]
axs[2].bar(labels, values, color=['blue', 'green'])
axs[2].set_title("Car Prices Comparison")
axs[2].set_ylabel("EUR")


# automatski raspored
plt.tight_layout()
plt.show()