# Game Documentation: Path of Survival

## Introduction
Path of Survival is a survival simulation game developed in Python. The primary goal is to survive as many days as possible by carefully managing your resources and making strategic decisions. Players need to balance attributes like food, water, energy, and health to avoid any of them reaching zero, which results in the end of the game.

## Requirements
° Python 3.8 or higher
° random library (native to Python)

## Player Attributes
° Food: Essential for survival. Decreases over time and can be replenished by searching for resources or through positive events.
° Water: Vital to keep the player alive. Like food, it is consumed daily and replenished through certain actions.
° Health: Represents the player's well-being. It can be affected by negative events and recovered by resting.
° Energy: Necessary to perform actions such as exploring and building. It can be recovered by resting.

## Game Rules
. The player must manage all four attributes. If any of them reach zero, the game ends.
. At each turn, the player selects an action from the following:
 1. Search for resources: Replenishes food and water but decreases energy.
 2. Rest: Recovers energy and health but consumes food and water.
 3. Explore: Triggers random events, both positive and negative, and decreases energy.
 4. Build shelter: Improves overall efficiency for future days but consumes energy.
. Basic resources (food, water, and energy) automatically decrease at the end of each day.

## Random Events
Events occur when the player chooses to explore:

. Storm: 50% chance of causing damage to health.
. Treasure: Rewards with additional food and water.
. Creature: Attacks the player, reducing health.
. Survivor:
  . Could be friendly, sharing resources.
  . Could be hostile, causing damage to health.

## Gameplay Flow
1. The player starts with 50 points in each attribute and is informed of the rules and losing conditions.
2. Each turn:
 . The game displays the current day and the player's attributes.
 . The player selects one of the available actions.
 . The system updates the attributes based on the chosen action and any triggered random events.
 . Resources are automatically consumed at the end of the day.
3. The game ends when any attribute reaches zero.
4. The total number of days survived is displayed at the end.

## Detailed Actions
1. Search for resources:
 . Gains 10 to 30 points of food and water.
. Loses 10 points of energy.
2. Rest:
 . Recovers 20 points of energy.
 . Recovers 10 points of health.
 . Consumes 10 points of food and water.
3. Explore:
 . Consumes 15 points of energy.
 . Triggers a random event (positive or negative).
4. Build shelter:
 . Consumes 20 points of energy

## Screenshots
![image](https://github.com/user-attachments/assets/2e9f1d90-4551-4c5a-87d1-84369f708241)

## Credits
Developer: [Rodrigo Kamiguchi] Graphics and Sound: Custom-created or sourced from open repositories (if applicable). Libraries Used: Python: https://www.python.org/ Pygame: https://www.pygame.org/

## License
This game is open-source and distributed under the MIT License. You are free to modify, distribute, and use the game as long as proper credit is given to the original developer(s). The full text of the license can be found in the LICENSE file.
## Conclusion
Path of Survival is a simple yet challenging game designed to test the player's ability to manage resources and make strategic decisions in a hostile environment. The combination of planning and random events ensures a unique experience with every session.
