# hass-bayesian-sensor-notebook
Jupyter notebook and class to easily test and create Home Assistant Bayesian sensors

## Installation
Copy the files to your notebooks folder inside and and run.

## Usage
Open bayesian_sensor.ipynb in Juypter Notebooks, it contains all the examples.

First add a bayesian sensor by calling Bayesian(name, prior, threshold)

```
presence = Bayesian('Tv in the evening', 0.3, 0.8)
```

Add one or more observations to the sensor by calling add_observation(name, probability_true, probability_false, platform, value, entity_id). Platform can be state, numeric_state or amount. The parameter value can be a string with the on_state value, a dict with min, max for the numeric_state or a string with the value_template.

```
presence.add_observation('home', 0.4, 0.15, 'state', 'zoning', 'zone.home')
```

You can get individual probabilities by calling get_formatted_probability and adding only one observation name in it.

```
presence.get_formatted_probability(['home'])
```

To get the probability of multiple observations add the names to the array

```
presence.get_formatted_probability(['home', 'evening', 'media'])
```

You can also get the probability value only by calling get_probability(['name_of_observation'])

Finally you can generate a Home Assistant Bayesian sensor by calling:
get_sensor()

```
presence.get_sensor()
```

## More information
[Bayesian Binary Sensor](https://www.home-assistant.io/components/bayesian/)