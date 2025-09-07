# 🎰 Powerball Number Predictor

A Python-based lottery number prediction system that combines random generation with statistical analysis to help you pick your lucky numbers!

## ✨ Features

- 🎲 **Random Picker**: Pure randomization for those who trust lady luck
- 🧠 **Smart Picker**: Statistical analysis of historical data patterns
- 📊 **Data Visualization**: Charts and graphs showing number frequencies
- 📈 **Trend Analysis**: Identify hot and cold numbers
- 💾 **Result Tracking**: Save and compare your predictions

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/powerball-predictor.git
cd powerball-predictor

# Install dependencies
pip install -r requirements.txt

# Run the predictor
python main.py
```

## 📁 Project Structure

```
powerball-predictor/
├── main.py                 # Main application entry point
├── random_picker.py        # Random number generation module
├── smart_picker.py         # Statistical analysis module
├── data/
│   ├── historical_data.csv # Historical Powerball results
│   └── predictions.json    # Saved predictions
├── utils/
│   ├── data_loader.py      # Data handling utilities
│   └── visualizer.py       # Chart generation
└── requirements.txt        # Python dependencies
```

## 🎲 Random Picker (`random_picker.py`)

The Random Picker generates completely random Powerball combinations using Python's cryptographically secure random number generator.

### Features:
- **True Randomization**: Uses `secrets` module for cryptographic randomness
- **Multiple Sets**: Generate 1-10 number combinations at once
- **Quick Play**: Fastest way to get lottery numbers
- **No Bias**: Each number has equal probability of selection

### Usage:
```python
from random_picker import RandomPicker

picker = RandomPicker()
numbers = picker.generate_numbers(count=5)  # Generate 5 sets
print(numbers)
```

### Output Example:
```
Set 1: [12, 28, 35, 47, 59] + Powerball: 18
Set 2: [03, 19, 24, 36, 51] + Powerball: 07
Set 3: [08, 15, 29, 42, 66] + Powerball: 23
```

## 🧠 Smart Picker (`smart_picker.py`)

The Smart Picker analyzes historical Powerball data to identify patterns and trends, using statistical methods to generate "intelligent" predictions.

### Features:
- **Frequency Analysis**: Tracks how often each number appears
- **Hot/Cold Numbers**: Identifies trending and overdue numbers
- **Pattern Recognition**: Analyzes number spacing and sum ranges
- **Weighted Selection**: Adjusts probabilities based on historical data
- **Multiple Strategies**: Choose from different analytical approaches

### Analysis Methods:
1. **Frequency-Based**: Favors most commonly drawn numbers
2. **Balanced Approach**: Mix of hot and cold numbers
3. **Pattern Matching**: Looks for recurring draw patterns
4. **Statistical Modeling**: Uses regression analysis for predictions

### Usage:
```python
from smart_picker import SmartPicker

# Initialize with historical data
picker = SmartPicker('data/historical_data.csv')

# Generate predictions using different strategies
hot_numbers = picker.generate_hot_picks(count=3)
balanced = picker.generate_balanced_picks(count=3)
pattern_based = picker.generate_pattern_picks(count=3)
```

### Smart Picker Strategies:

#### 🔥 Hot Numbers Strategy
- Focuses on frequently drawn numbers from recent draws
- Analyzes last 100-500 drawings depending on configuration
- Weights selection toward "hot" numbers

#### ❄️ Cold Numbers Strategy  
- Targets numbers that haven't appeared recently
- Based on the theory that overdue numbers are "due"
- Balances statistical probability with gap analysis

#### ⚖️ Balanced Strategy
- Combines hot and cold number analysis
- Maintains optimal number distribution across ranges
- Uses sum range analysis for realistic combinations

## 📊 Data Sources

The system uses historical Powerball data including:
- Drawing dates from 2010-present
- Main numbers (1-69) and Powerball numbers (1-26)
- Jackpot amounts and winner information
- Statistical breakdowns and frequency charts

## 🛠️ Requirements

```
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.5.0
seaborn>=0.11.0
requests>=2.25.0
```

## 📈 Visualization Features

- **Number Frequency Charts**: Bar graphs showing draw frequency
- **Hot/Cold Heatmaps**: Visual representation of number trends
- **Timeline Analysis**: Number appearance over time
- **Sum Distribution**: Analysis of winning number sum ranges

## ⚙️ Configuration

Customize the predictor behavior in `config.py`:

```python
CONFIG = {
    'analysis_period': 500,        # Number of recent draws to analyze
    'hot_threshold': 0.7,          # Hot number threshold
    'cold_threshold': 0.3,         # Cold number threshold
    'prediction_count': 5,         # Default predictions to generate
    'visualization': True          # Enable/disable charts
}
```

## 🎯 Usage Examples

### Generate Random Numbers
```python
python main.py --mode random --count 10
```

### Smart Analysis with Visualization
```python
python main.py --mode smart --strategy balanced --visualize
```

### Export Results
```python
python main.py --mode smart --export results.json
```

## ⚠️ Disclaimer

**This tool is for entertainment purposes only.** Lottery numbers are drawn randomly, and no system can guarantee winning numbers. Past results do not influence future draws. Please gamble responsibly and only spend what you can afford to lose.

The mathematical probability of winning the Powerball jackpot is approximately 1 in 292,201,338, regardless of the number selection method used.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:
- New statistical analysis methods
- Additional data sources
- UI improvements
- Bug fixes and optimizations

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎲 Good Luck!

Remember, every ticket is a winner... of hope! May the odds be ever in your favor! 🍀

---

*"You miss 100% of the shots you don't take... and 99.99999% of the ones you do take in the lottery!"* 😄
