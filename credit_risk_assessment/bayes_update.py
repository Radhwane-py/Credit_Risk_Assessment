def bayes_theorem(prior, likelihood, evidence):
    return (likelihood * prior) / evidence

def update_risk_profile(risk_profiles, new_data):
    updated_profiles = {}
    for score, risk in risk_profiles.items():
        prior = risk
        likelihood = new_data.get(score, 0.5) 
        evidence = sum(new_data.values()) / len(new_data)
        updated_profiles[score] = bayes_theorem(prior, likelihood, evidence)
    return updated_profiles
