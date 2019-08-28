class Bayesian:
    def __init__(self, name, prior, threshold):
        self.name = name
        self.prior = prior
        self.threshold = threshold
        self.observations = {}


    def calculate_probability(self, prior, prob_true, prob_false):
        numerator = prob_true * prior
        denominator = numerator + prob_false * (1 - prior)
        probability = numerator / denominator
        return round(probability, 2)


    def get_probability(self, observations):
        probability = self.prior

        for item in observations:
            observation = self.observations[item]
            probability = self.calculate_probability(probability, observation['prob_true'], observation['prob_false'])

        return probability


    def get_formatted_probability(self, observations):
        probability = self.get_probability(observations)
        print(self.name + ': ' + ('on' if probability >= self.threshold else 'off') + ' (' + str(probability) + ')')


    def add_observation(self, name, prob_true, prob_false, platform, value, entity_id=None):
        self.observations[name] = {
            'entity_id': entity_id,
            'platform': platform,
            'value': value,
            'prob_true': prob_true,
            'prob_false': prob_false
        }


    def get_sensor(self):
        res = '- platform: bayesian\n'
        res += f'  name: {self.name}\n'
        res += f'  prior: {str(self.prior)}\n'
        res += f'  probability_threshold: {str(self.threshold)}\n'
        res += f'  observations:\n'

        for item in self.observations:
            obs = self.observations[item]
            if obs['platform'] == 'state':
                res += '    - platform: state\n'
                res += f'      entity_id: {obs["entity_id"]}\n'
                res += f'      to_state: "{obs["value"]}"\n'
            elif obs['platform'] == 'numeric_state':
                res += '    - platform: numeric_state\n'
                res += f'      entity_id: {obs["entity_id"]}\n'
                res += f'      min: {obs["value"]["min"]}\n'
                res += f'      max: {obs["value"]["max"]}\n'
            elif obs['platform'] == 'template':
                res += '    - platform: value_template\n'
                res += f'      value_template: >-\n        {obs["value"]}\n'

            res += f'      prob_given_true: {obs["prob_true"]}\n'
            res += f'      prob_given_false: {obs["prob_false"]}\n'
        print(res)