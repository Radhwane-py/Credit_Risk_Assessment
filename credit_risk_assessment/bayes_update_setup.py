from collections import OrderedDict

def bayes_theorem(prior, likelihood, evidence):
    return (likelihood * prior) / evidence

def update_risk_profile(risk_profiles, new_data):
    # Update risk profiles based on existing scores in risk_profiles.
    updated_profiles = {}
    for score, risk in risk_profiles.items():
        prior = risk
        likelihood = new_data.get(score, 0.5) 
        evidence = sum(new_data.values()) / len(new_data)
        updated_profiles[score] = bayes_theorem(prior, likelihood, evidence)

    # Add new scores from new_data that are not in risk_profiles.
    for score, likelihood in new_data.items():
        if score not in risk_profiles:
            updated_profiles[score] = likelihood 

    sorted_updated_profiles = OrderedDict(sorted(updated_profiles.items()))

    return sorted_updated_profiles
