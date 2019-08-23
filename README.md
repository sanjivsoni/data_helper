# Data Formatter

Data Formatter is a Python library for creating plots and summary tables.

## Getting Started

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install prerequisites for Data Formatter. You need Pandas, Matplotlib and Numpy. This code is written in Python3

```bash
pip install pandas numpy matplotlib
```

## Usage

```python
import data_formatting as df

# returns dataframe
df.create_stats_table(data = filtered_df, 
                      filter_bins=age_bins,
                      filter_column='age',
                      features=features) 

# Plots a histogram for a feature with std and mean in title
df.plot_hist(df = data['feature'],
             bins = 20,
             title = 'Distribution of Feature',
             xlabel = 'Bins',
             ylabel = 'frequency',
             lower_limit = 0,
             upper_limit = 1
         ) 

# Plots a decile plot
mf.create_decile_plot(df = data,
                      title = "Sample Decile Plot Title",
                      n_bins = 10)

# Plots columns of a dataframe as defined in the spec
mf.plot_df_features(df data,
                    spec_plot = spec,
                    spec_xlabel = xlabel,
                    suptitle = super_title)
```

## Screenshots
Creating a Decile Plot
![Screenshot 2019-08-23 at 10 02 24 AM](https://user-images.githubusercontent.com/6757985/63609990-2f87cb80-c58d-11e9-88f1-598f1fd081b5.png)

Creating a Statistical Summary Table
![Screenshot 2019-08-23 at 10 06 50 AM](https://user-images.githubusercontent.com/6757985/63610214-bfc61080-c58d-11e9-8182-931f88617817.png)

Creasting Histogram Pplot
![Screenshot 2019-08-23 at 10 08 53 AM](https://user-images.githubusercontent.com/6757985/63610310-074c9c80-c58e-11e9-9810-56836f404d7f.png)



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
