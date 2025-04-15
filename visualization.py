# graph info
# numbers are not current, uploading codebase

import matplotlib.pyplot as plt
import numpy as np

# regional attendees
regions = ['Ottawa', 'Atlanta', 'Boston', 'New York']
attendees = [1, 1, 1, 1]
colors = ['lightblue', 'purple', 'red', 'orange']

plt.figure(figsize=(5, 3))
plt.bar(regions, attendees, color=colors)

plt.title('Attendees Across Regions')
plt.xlabel('Region')
plt.ylabel('Number of Attendees')
plt.show()

# projects shipped across regions
regions = ['Ottawa', 'Atlanta', 'Boston', 'SF', 'NYC']
projects = [1, 1, 1, 1, 1]
colors = ['lightblue', 'purple', 'red', 'green', 'indigo']

plt.figure(figsize=(5, 5))
plt.bar(regions, projects, color=colors)
plt.title('Projects Deployed Across Regions')
plt.xlabel('Region')
plt.ylabel('Number of Projects')
plt.show()

# attendees versus projects shipped across regions
regions = ['Ottawa', 'Atlanta', 'Boston', 'SF', 'NYC']
attendees = [1, 1, 1, 1, 1]
projects = [1, 1, 1, 1, 1]
colors = ['lightblue', 'purple', 'red', 'orange', 'green']

slope, intercept = np.polyfit(attendees, projects, 1)
regression_line = [slope * x + intercept for x in attendees]
plt.figure(figsize=(7, 6))

for i in range(len(regions)):
    plt.scatter(attendees[i], projects[i], color=colors[i], s=100)
    plt.text(attendees[i] + 1, projects[i], regions[i], fontsize=9)

x_vals = np.linspace(min(attendees), max(attendees), 100)
y_vals = slope * x_vals + intercept
plt.plot(x_vals, y_vals, color='black', linestyle='--', linewidth=1.5, label='Regression Line')

plt.title('Attendees vs. Projects Deployed by Region')
plt.xlabel('Number of Attendees')
plt.ylabel('Number of Projects Deployed')
plt.grid(True)
plt.tight_layout()
plt.show()

# radar chart on program performance
labels = [
    'Onboarding Completion',
    'Agents Deployed',
    'Total Event Attendance',
    'Returning Builders',
    'Applicant-to-Builder Conversion'
]

raw_values = {
    'Onboarding Completion': 80,
    'Agents Deployed': (20 / 25) * 100,
    'Total Event Attendance': (476 / 600) * 100,
    'Returning Builders': 68,
    'Applicant-to-Builder Conversion': 50
}

values = list(raw_values.values())
values += values[:1]

num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.plot(angles, values, color='teal', linewidth=2)
ax.fill(angles, values, color='teal', alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=11)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(['20', '40', '60', '80', '100'])
ax.set_ylim(0, 100)

plt.title('How the NEAR AI Agent Program is Performing', size=14, weight='bold', y=1.08)
ax.spines['polar'].set_visible(False)
ax.grid(color='gray', linestyle='dotted', linewidth=0.8)
ax.tick_params(colors='gray')

plt.tight_layout()
plt.show()

# exp vs act
plt.style.use('dark_background')

labels = [
    'Onboarding Completion',
    'Agents Deployed',
    'Total Event Attendance',
    'Returning Builders',
    'Applicant-to-Builder Conversion'
]

actual = {
    'Onboarding Completion': 80,
    'Agents Deployed': (20 / 25) * 100,
    'Total Event Attendance': (476 / 600) * 100,
    'Returning Builders': 68,
    'Applicant-to-Builder Conversion': 50
}

expected = {
    'Onboarding Completion': 90,
    'Agents Deployed': 100,
    'Total Event Attendance': 100,
    'Returning Builders': 75,
    'Applicant-to-Builder Conversion': 60
}

actual_values = list(actual.values()) + [list(actual.values())[0]]
expected_values = list(expected.values()) + [list(expected.values())[0]]

num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

ax.plot(angles, actual_values, color='#8a2be2', linewidth=2, label='Actual')
ax.fill(angles, actual_values, color='#1e90ff', alpha=0.3)

ax.plot(angles, expected_values, color='orange', linewidth=1.5, linestyle='dashed', label='Predicted')
ax.fill(angles, expected_values, color='orange', alpha=0.1)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=11, color='white')
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(['20', '40', '60', '80', '100'], color='white')
ax.set_ylim(0, 100)

ax.spines['polar'].set_visible(False)
ax.grid(color='white', linestyle='dotted', linewidth=0.8)
ax.tick_params(colors='white')

plt.title('Program Performance: Expected vs Actual', size=14, weight='bold', y=1.08, color='white')
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), facecolor='black', edgecolor='white', labelcolor='white')

plt.tight_layout()
plt.show()

