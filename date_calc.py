import juliandate as jd
from datetime import datetime


def get_date_from_user(prompt="Enter observation date (DD-MM-YYYY):\n"):
    """
    Function that asks the user for a date and ensures it's in the correct format.
    """
    while True:
        user_input = input(prompt)
        try:
            date = datetime.strptime(user_input, "%d-%m-%Y")
            return date
        except ValueError:
            print("Incorrect format! Please enter the date in DD-MM-YYYY format.")

def calc_next_eclipse(p, m0):
    """
    Function to calculate the next eclipse date based on the orbital period and initial date (m0).
    """
    now = datetime.now()
    m_obs = jd.from_gregorian(now.year, now.month, now.day)
    e1 = (m_obs - m0) / p
    e2 = int(e1) + 1
    mc = m0 + p * e2
    return mc

def main():
    # Get the observation date from the user
    obs_date = get_date_from_user()

    # Calculate the next eclipse date
    p = 0.44974999  # Orbital period in days
    m0 = 2446449.7811  # Initial eclipse date [JD]
    mc = calc_next_eclipse(p, m0)
    
    # List of the next 10 eclipses
    d_list = []
    for i in range(500):
        mc2 = mc + (p * (i + 1))
        date = datetime(*jd.to_gregorian(mc2))
        if (date.year >= obs_date.year and 
            date.month >= obs_date.month and 
            date.day >= obs_date.day):
            d_list.append(date.strftime("%d-%m-%Y %H:%M:%S"))
    
    sorted_dates = sorted(d_list, key=lambda x: int(x[8:10]))[:10]
    for eclipse in sorted_dates:
        print("Next eclipse:", eclipse)

if __name__ == "__main__":
    main()