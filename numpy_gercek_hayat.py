import numpy as np
import matplotlib.pyplot as plt

# ----- BÖLÜM 1: Şirket Maaş Analizi -----

# Rastgele maaş verisi oluşturur.
np.random.seed(42)
employees_salary = np.random.randint(10000, 50000, 500)
departments = np.random.choice([1, 2, 3], 500)

# Ortalama, maksimum ve minimum maaş hesaplama
mean_salary = np.mean(employees_salary)
max_salary = np.max(employees_salary)
min_salary = np.min(employees_salary)

# Departman bazında ortalama maaş hesaplama
department_names = {1: "Engineering", 2: "Accounting", 3: "Marketing"}
department_mean_salary = {name: np.mean(employees_salary[departments == dept]) for dept, name in department_names.items()}

# Histogram çizimi
plt.figure(figsize=(12, 6))
colors = ['blue', 'green', 'red']
max_y_value = 0  # Y-eksenini ayarlamak için maksimum değer

for (department, salaries), color in zip(department_mean_salary.items(), colors):
    data = employees_salary[departments == list(department_names.keys())[list(department_names.values()).index(department)]]
    counts, bins, patches = plt.hist(data, bins=30, alpha=0.5, label=f"{department} (Ortalama: {salaries:.2f} TL, {len(data)} Çalışan)", color=color)
    max_y_value = max(max_y_value, max(counts))  # Maksimum çalışan sayısını bul

# Ortalama, maksimum ve minimum maaşları çizgi olarak gösterir
plt.axvline(mean_salary, color='black', linestyle='dashed', linewidth=2, label=f"Genel Ortalama: {mean_salary:.2f} TL")
plt.axvline(max_salary, color='purple', linestyle='dotted', linewidth=2, label=f"Maks: {max_salary} TL")
plt.axvline(min_salary, color='orange', linestyle='dotted', linewidth=2, label=f"Min: {min_salary} TL")

# Y-eksenini otomatik olarak ayarlar
plt.ylim(0, max_y_value + 5)
plt.xlabel("Maaş (TL)")
plt.ylabel("Çalışan Sayısı")
plt.title("Departmanlara Göre Maaş Dağılımı")
plt.legend()
plt.grid(True)
plt.show()


# ----- BÖLÜM 2: Hava Durumu Verileri Üretme ve Analiz -----


# Günlük sıcaklık değerlerini simüle etme
days = 365
# -10°C ile 40°C arasında rastgele sıcaklıklar üretir.
temperature_data = np.random.randint(-10, 41, size=days)

# Ortalama sıcaklığı bulur.
average_temperature = np.mean(temperature_data)

# En sıcak ve en soğuk günleri değişkene ekler.
max_temperature_day = np.argmax(temperature_data)
min_temperature_day = np.argmin(temperature_data)

# Günlük sıcaklık değişimlerinin çizgi grafiğini oluşturmak için
plt.figure(figsize=(10, 5))
plt.plot(temperature_data, label="Daily Temperature")
plt.title("Daily Temperature Over the Year")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()

#  Ürün Satış Analizi

# Ürün isimleri
products = ["Phone", "Computer", "Headphones", "Watch", "Tablet"]

# Satış miktarlarını simüle etmek için (her ürün için 30 günlük satış)
sales_data = {product: np.random.randint(10, 101, size=30) for product in products}

# Her ürünün toplam ve ortalama satış miktarlarını hesaplama
sales_summary = {
    product: {
        "total_sales": np.sum(sales_data[product]),
        "average_sales": np.mean(sales_data[product])
    }
    for product in products
}

# Ürün bazında çubuk grafiği çizme
total_sales = [sales_summary[product]["total_sales"] for product in products]
plt.figure(figsize=(10, 6))
plt.bar(products, total_sales, color='skyblue')
plt.title("Total Sales for Each Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Sonuçlar
average_temperature, max_temperature_day, min_temperature_day, sales_summary
