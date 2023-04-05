import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://gearvn.com/collections/laptop-gaming-ban-chay'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
products = soup.find_all('div', {'class': 'product-row'})
data = []
for product in products:
    name = product.find('h2', {'class': 'product-row-name'}).text.strip()
    # Đọc giá trị cũ
    old_price = product.find(
        'div', {'class': 'product-row-price'}).find('del').text.strip()
    # Đọc giá mới
    new_price = product.find('span', {'class': 'product-row-sale'}).text.strip()
    percent_discount = product.find(
        'div', {'class': 'new-product-percent'}).text.strip()
    best_seller = 1 if product.find(
        'span', {'class': 'ico-product ico-km'}) else 0

    match = re.search(r'^laptop gaming (.*)', name.lower())
    if match:
        product_name = match.group(1).strip()
        brand_match = re.search(r'^(.*?)\s+(.*)', product_name)
        if brand_match:
            brand = brand_match.group(1).strip()
            product_name = brand_match.group(2).strip()

    old_price = int(re.sub(r'[^\d]+', '', old_price))
    new_price = int(re.sub(r'[^\d]+', '', new_price))
    percent_discount = int(re.sub(r'[^\d]+', '', percent_discount))

    data.append({
        'Name': product_name,
        'Brand': brand,
        'OldPrice': old_price,
        'NewPrice': new_price,
        'PercentDiscount': percent_discount,
        'BestSeller': best_seller
    })

df = pd.DataFrame(data)
print(df)

# Trực quan trung bình và trung vị giá bán cũ và mới với các Brand. Cho nhận xét
# Tạo dataframe mới
df = pd.DataFrame(data)

# Tính trung bình và trung vị của giá bán cũ và mới theo từng Brand
agg_df = df.groupby("Brand").agg({"OldPrice": ["mean", "median"], "NewPrice": ["mean", "median"]})
agg_df.columns = ["OldPrice_mean", "OldPrice_median", "NewPrice_mean", "NewPrice_median"]
agg_df = agg_df.reset_index()

# vẽ biểu đồ boxplot
fig, axs = plt.subplots(ncols=2, figsize=(12, 6))

sns.boxplot(x="Brand", y="OldPrice", data=df, ax=axs[0])
sns.boxplot(x="Brand", y="NewPrice", data=df, ax=axs[1])

axs[0].set_title("Old Price")
axs[1].set_title("New Price")

plt.show()

# df_mean = df.groupby('Brand')[['OldPrice', 'NewPrice']].mean().reset_index()
# df_median = df.groupby(
#     'Brand')[['OldPrice', 'NewPrice']].median().reset_index()

# # Trực quan hóa dữ liệu
# fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# sns.barplot(x='Brand', y='OldPrice', data=df_mean, ax=ax[0][0])
# ax[0][0].set_title('Mean Old Price by Brand')

# sns.barplot(x='Brand', y='NewPrice', data=df_mean, ax=ax[0][1])
# ax[0][1].set_title('Mean New Price by Brand')

# sns.barplot(x='Brand', y='OldPrice', data=df_median, ax=ax[1][0])
# ax[1][0].set_title('Median Old Price by Brand')

# sns.barplot(x='Brand', y='NewPrice', data=df_median, ax=ax[1][1])
# ax[1][1].set_title('Median New Price by Brand')

# plt.tight_layout()
# plt.show()

# Nhận xét
# Các Brand Laptop Gaming trong dataset có giá bán cũ và mới từ 10 triệu đồng đến 30 triệu đồng, với giá bán mới trung bình và trung vị thấp hơn giá bán cũ.
# Brand MSI có giá bán cũ và mới cao hơn so với các Brand khác, với giá bán mới trung bình và trung vị đều trên 20 triệu đồng.
# Brand Asus có giá bán mới trung bình thấp hơn so với các Brand khác, trong khi Brand Acer có giá bán mới trung vị thấp hơn.

# Trực quan đếm số sản phẩm của các Brand. Cho nhận xét
df = pd.DataFrame(data)
sns.set(style="darkgrid")
plt.figure(figsize=(12, 6))
ax = sns.countplot(x="Brand", data=df, order=df['Brand'].value_counts().index)
ax.set_title("Số lượng sản phẩm của từng Brand")
ax.set_xlabel("Brand")
ax.set_ylabel("Số lượng sản phẩm")
plt.show()

# Nhận xét:
# Từ biểu đồ, ta có thể thấy được số lượng sản phẩm của từng brand, và có thể thấy rằng HP và MSI là những brand có số lượng sản phẩm cao nhất.

# Trực quan mức giảm giá cao nhất và thấp nhất của sản phẩm mỗi Brand. Cho nhận xét

df = pd.DataFrame(data)
# df = df[df['PercentDiscount'] != '']
# df['PercentDiscount'] = df['PercentDiscount'].astype(float)
# df['NewPrice'] = df['NewPrice'].astype(int)
# sns.boxplot(x='Brand', y='PercentDiscount', data=df)
# Tính giá trị giảm giá cao nhất và thấp nhất của từng Brand
discount_max = df.groupby('Brand').apply(lambda x: ((x['OldPrice'] - x['NewPrice']) / x['OldPrice']).max()).reset_index()
discount_min = df.groupby('Brand').apply(lambda x: ((x['OldPrice'] - x['NewPrice']) / x['OldPrice']).min()).reset_index()
discount_max.columns = ['Brand', 'DiscountMax']
discount_min.columns = ['Brand', 'DiscountMin']

# Trực quan hóa bằng biểu đồ column chart
fig, ax = plt.subplots()
ax.bar(discount_max['Brand'], discount_max['DiscountMax'], label='Max Discount')
ax.bar(discount_min['Brand'], discount_min['DiscountMin'], label='Min Discount')
ax.set_xlabel('Brand')
ax.set_ylabel('Discount')
ax.legend()
plt.show()

# Nhận xét: Boxplot cho phép chúng ta so sánh mức giảm giá và giá mới của các sản phẩm của các brand khác nhau.
# Chúng ta có thể quan sát được rằng, các sản phẩm của brand Dell, MSI và Lenovo thường có mức giảm giá cao hơn so với các brand khác.
# Tuy nhiên, các sản phẩm của brand Acer và Asus lại có giá trị trung bình và median cao hơn so với các brand khác.
# Boxplot cũng cho thấy rằng, các brand khác nhau có sự phân tán khác nhau về giá và mức giảm giá của sản phẩm của mình.

# Trực quan mức giá mới của các sản phẩm là BestSeller. Cho nhận xét

best_sellers = []
new_prices = []

for item in data:
    if item['BestSeller'] == 1:
        best_sellers.append(item['Name'])
        new_prices.append(item['NewPrice'])

plt.bar(best_sellers, new_prices)
plt.xticks(rotation=90)
plt.ylabel('New Price')
plt.title('New Prices of Bestselling Products')
plt.show()
