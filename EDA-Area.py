# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
import pandas as pd 
import numpy as np 
import matplotlib
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt
import seaborn as sns
from warnings import filterwarnings
get_ipython().run_line_magic('matplotlib', 'inline')
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px


# %%
df = pd.read_csv(("sample_data.csv"))
df


# %%
df.info()


# %%
# from pandas_profiling import ProfileReport

# profile = ProfileReport(df)
# profile.to_file(output_file = "area_details.html" ) # creation of pandas profile report for easy understanding of the data


# %%
df.shape 

# %% [markdown]
# ### In Data Analysis We will Analyze To Find out the below stuff ###
# ### 1. Missing Values ###
# ### 2. All The Numerical Variables ###
# ### 3. Distribution of the Numerical Variables ###
# ### 4. Categorical Variables ###
# ### 5. Outliers ###
# ### 6. Relationship between independent and dependent feature(SalePrice) ###
# %% [markdown]
# # ** 1. Missing Values**
# 

# %%
## Here we will check the percentage of nan values present in each feature

## 1 -step make the list of features which has missing values

features_with_na=[features for features in df.columns if df[features].isnull().sum()>1] #list comprehension use

## 2- step print the feature name and the percentage of missing values

for feature in features_with_na:
    print(feature, np.round(df[feature].isnull().mean(), 4),  ' % missing values')

# %% [markdown]
# ### There are no missing values in the data set 
# %% [markdown]
# # ** 2. All The Numerical Variables **

# %%
numerical_features = [feature for feature in df.columns if df[feature].dtypes != 'O'] # list comprehension feature that are not equal to object type

print('Number of numerical variables: ', len(numerical_features))

df[numerical_features].head()

# %% [markdown]
# ## *let us check for decreate values*

# %%
## Numerical variables are usually of 2 type
## 1. Continous variable and Discrete Variables

discrete_feature=[feature for feature in numerical_features if len(df[feature].unique())<25]
print("Discrete Variables Count: {}".format(len(discrete_feature)))


# %%
discrete_feature


# %%
df.head()


# %%
a = 2  # number of rows
b = 2  # number of columns
c = 1  # initialize plot counter

fig = plt.figure(figsize=(20,15))

for i in discrete_feature:
    plt.subplot(a, b, c)
    plt.title('{} vs Price, subplot'.format(i))

    sns.scatterplot(x= i, y = "price" ,data=df, hue = "type" )
      
    # plt.title(f" Gender vs {i}")

    c = c + 1

plt.show()


# %%
a = 2  # number of rows
b = 1  # number of columns
c = 1  # initialize plot counter

fig = plt.figure(figsize=(40,35))

for i in discrete_feature:
    plt.subplot(a, b, c)
    plt.title('{} vs Price, subplot'.format(i))

    sns.barplot(x= i, y = "price" ,data=df, hue = "type" )
      
    # plt.title(f" Gender vs {i}")

    c = c + 1

plt.show()


# %%
a = 2  # number of rows
b = 2  # number of columns
c = 1  # initialize plot counter

fig = plt.figure(figsize=(20,15))

for i in discrete_feature:
    plt.subplot(a, b, c)
    plt.title('{} vs Price'.format(i))

    sns.boxplot(x= i, y = "price" ,data=df, hue = "type" )
      
    # plt.title(f" Gender vs {i}")

    c = c + 1

plt.show()

# %% [markdown]
# ## ** Continous Features **

# %%
continuous_feature=[feature for feature in numerical_features if feature not in discrete_feature ]
print("Continuous feature Count {}".format(len(continuous_feature)))


# %%
continuous_feature

# %% [markdown]
# ### We are not plotting latitude & longitude values 

# %%
a = 3  # number of rows
b = 1 # number of columns
c = 1  # initialize plot counter

# fig = plt.figure(figsize=(20,55))
fig = plt.figure(figsize=(20,30))
for i in continuous_feature[0:3]:

    plt.subplot(a, b, c)
    plt.title('{}  , subplot: {}{}{}'.format(i, a, b, c))

    sns.scatterplot(data= df, x= i, y = "price", hue="type",palette="deep", size= "type" )

    c = c + 1

plt.show()


# %%

fig = plt.figure(figsize=(30,40))

for i in continuous_feature[0:3]:
    g = sns.relplot(data= df, x= i, y = "price", col="type", hue="type",kind="scatter")
    g.fig.suptitle(f"{i} Vs Price", fontweight ="bold")
    plt.subplots_adjust(top=0.85)

plt.show()


# %%
a = 3  # number of rows
b = 1 # number of columns
c = 1  # initialize plot counter

# fig = plt.figure(figsize=(20,55))
fig = plt.figure(figsize=(20,30))
for i in continuous_feature[0:3]:

    plt.subplot(a, b, c)
    plt.title('{}  , subplot: {}{}{}'.format(i, a, b, c))


    sns.histplot(data= df, x= i, y = "price", hue="type", stat="density", common_norm=False,)
    

    
    

    c = c + 1

plt.show()

# %% [markdown]
# ## latitude & longitude values 

# %%
plt.figure(figsize=(40,30))
sns.displot(data= df, x=  'latitude' , y= 'longitude', kind="kde", hue= "type", col="type")

g.fig.suptitle("Latitude & longitude positions of the houses", fontweight ="bold")
plt.subplots_adjust(top=0.85)
plt.show()

# %% [markdown]
# # **OUTLIERS **

# %%
a = 2  # number of rows
b = 1  # number of columns
c = 1  # initialize plot counter

fig = plt.figure(figsize=(30, 25))

plt.style.use("ggplot")

for i in continuous_feature[0:3]:
    data=df.copy()

    if 0 in data[i].unique():
        pass
    else:
        plt.subplot(a, b, c)
        plt.title('price Vs {} '.format(i))

        sns.scatterplot(x=i , y = "price" ,data=df, hue= "type")

        c = c + 1

# %% [markdown]
# ## ** categorical vairables **

# %%
categorical_features=[feature for feature in df.columns if df[feature].dtypes=='O']
categorical_features


# %%
for feature in categorical_features:
    print('The feature is {} and number of categories are {}'.format(feature,len(df[feature].unique())))


# %%
df.street.value_counts()

# %% [markdown]
# ### There are many streeets with just 1 loaction, so We'll avoid it for plotting

# %%
categorical_features[1:]


# %%
a = 3  # number of rows
b = 1  # number of columns
c = 1  # initialize plot counter

fig = plt.figure(figsize=(20,15))
plt.style.use("ggplot")

for i in categorical_features[2:]:
    plt.subplot(a, b, c)
    plt.title('{} '.format(i))
    df[i].value_counts().plot(kind='pie', autopct='%.4f')
    plt.legend( bbox_to_anchor=(0.85,1.025), loc="upper left")
    

    c = c + 1

plt.show()


# %%
a = 3  # number of rows
b = 2  # number of columns
c = 1  # initialize plot counter

fig = plt.figure(figsize=(20, 25))
plt.style.use("ggplot")

for i in categorical_features[2:]:
    plt.subplot(a, b, c)
    plt.title('{} '.format(i))
    sns.barplot(x = df[i], y = df["price"] , hue = df["type"])
    plt.xticks(rotation=90)
    

    c = c + 1

plt.show()


# %%

plt.figure(figsize=(30,45))
sns.barplot(y = df["price"], x = df.city.head(200) , hue = df["type"], capsize=.2)
plt.title("topi cities Vs Price")
plt.xticks(rotation=90)

plt.show()


# %%



