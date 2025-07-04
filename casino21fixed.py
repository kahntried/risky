import streamlit as st
import random
import time
from typing import List, Tuple

# Page config
st.set_page_config(
    page_title="🃏 Blackjack",
    page_icon="🃏",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# Custom CSS for styling and animations
def get_theme_css(theme):
    base_styles = """
        .main-header {
            text-align: center;
            font-size: 1.8rem;
            margin-bottom: 0.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
        }
        .card {
            display: inline-block;
            background: white;
            border-radius: 10px;
            padding: 15px 10px;
            margin: 6px;
            box-shadow: 0 6px 12px rgba(0,0,0,0.5);
            font-size: 1.8rem;
            min-width: 70px;
            min-height: 95px;
            text-align: center;
            transition: transform 0.3s ease;
            border: 2px solid #ddd;
            animation: cardSlideIn 0.6s ease-out;
        }
        .card:nth-child(1) { animation-delay: 0.1s; }
        .card:nth-child(2) { animation-delay: 0.3s; }
        .card:nth-child(3) { animation-delay: 0.5s; }
        .card:nth-child(4) { animation-delay: 0.7s; }
        .card:nth-child(5) { animation-delay: 0.9s; }
        .card:nth-child(6) { animation-delay: 1.1s; }
        @keyframes cardSlideIn {
            0% { opacity: 0; transform: translateY(-30px) scale(0.8); }
            100% { opacity: 1; transform: translateY(0) scale(1); }
        }
        .card:hover { transform: translateY(-3px) scale(1.05); }
        .card-red { color: #DC143C; }
        .card-black { color: #2F4F4F; }
        .player-section, .dealer-section {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 15px;
            margin: 10px auto;
            max-width: 500px;
            backdrop-filter: blur(10px);
            text-align: center;
        }
        .cards-container { display: flex; justify-content: center; flex-wrap: wrap; margin: 10px 0; }
        .section-title {
            font-size: 1.1rem;
            font-weight: bold;
            margin-bottom: 10px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
        }
        .win-message, .lose-message {
            font-size: 1.5rem;
            font-weight: bold;
            text-align: center;
            animation: pulse 2s infinite;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
        }
        .win-message { color: #32CD32; }
        .lose-message { color: #FF6B6B; }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        .balance-display {
            font-size: 1.3rem;
            font-weight: bold;
            text-align: center;
            margin: 8px 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
        }
        .bet-section {
            padding: 20px 15px;
            border-radius: 12px;
            margin: 15px auto;
            max-width: 350px;
            backdrop-filter: blur(5px);
        }
        .bet-title {
            font-size: 1.2rem;
            font-weight: bold;
            text-align: center;
            margin-bottom: 15px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
        }
        .bet-subtitle {
            color: #FFF;
            font-size: 0.9rem;
            text-align: center;
            margin-bottom: 20px;
            opacity: 0.8;
        }
        .current-bet {
            text-align: center;
            font-size: 1.2rem;
            font-weight: bold;
            margin: 10px 0;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
        }
        .stats-container, .sidebar-info, .theme-selector {
            background: rgba(0,0,0,0.3);
            padding: 15px;
            border-radius: 10px;
            margin: 15px 0;
            backdrop-filter: blur(5px);
        }
        .game-action-buttons { text-align: center; margin: 15px 0; }
        .split-hand-title {
            font-size: 1rem;
            font-weight: bold;
            margin: 5px 0;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
        }
        .active-hand { box-shadow: 0 0 15px rgba(255, 215, 0, 0.5); }
    """

    if theme == "Classic Green":
        return f"""<style>
            .stApp {{
                background: radial-gradient(ellipse at center, #0d4f3c 0%, #1a6b47 35%, #134e3a 100%);
                background-attachment: fixed;
            }}
            .main-header, .score, .section-title, .balance-display, .current-bet, .bet-title, .split-hand-title {{
                color: #FFD700;
            }}
            .player-section, .dealer-section {{
                border: 2px solid rgba(255, 215, 0, 0.3);
            }}
            .bet-section {{
                background: rgba(255, 215, 0, 0.2);
                border: 2px solid #FFD700;
            }}
            .stats-container, .sidebar-info, .theme-selector {{
                border: 1px solid rgba(255, 215, 0, 0.3);
                color: #FFD700;
            }}
            .active-hand {{
                border: 3px solid #FFD700 !important;
            }}
            {base_styles}
        </style>"""

    elif theme == "Vegas Gold":
        return f"""<style>
            .stApp {{
                background: radial-gradient(ellipse at center, #8B4513 0%, #DAA520 35%, #B8860B 100%);
                background-attachment: fixed;
            }}
            .main-header, .score, .section-title, .balance-display, .current-bet, .bet-title, .split-hand-title {{
                color: #FFD700;
            }}
            .player-section, .dealer-section {{
                border: 2px solid rgba(255, 215, 0, 0.3);
            }}
            .bet-section {{
                background: rgba(255, 215, 0, 0.2);
                border: 2px solid #FFD700;
            }}
            .stats-container, .sidebar-info, .theme-selector {{
                border: 1px solid rgba(255, 215, 0, 0.3);
                color: #FFD700;
            }}
            .active-hand {{
                border: 3px solid #FFD700 !important;
            }}
            {base_styles}
        </style>"""

    elif theme == "Royal Purple":
        return f"""<style>
            .stApp {{
                background: radial-gradient(ellipse at center, #2D1B69 0%, #663399 35%, #4B0082 100%);
                background-attachment: fixed;
            }}
            .main-header, .score, .section-title, .balance-display, .current-bet, .bet-title, .split-hand-title {{
                color: #E6E6FA;
            }}
            .player-section, .dealer-section {{
                border: 2px solid rgba(230, 230, 250, 0.3);
            }}
            .bet-section {{
                background: rgba(230, 230, 250, 0.2);
                border: 2px solid #E6E6FA;
            }}
            .stats-container, .sidebar-info, .theme-selector {{
                border: 1px solid rgba(230, 230, 250, 0.3);
                color: #E6E6FA;
            }}
            .active-hand {{
                border: 3px solid #E6E6FA !important;
            }}
            {base_styles}
        </style>"""

    elif theme == "Midnight Blue":
        return f"""<style>
            .stApp {{
                background: radial-gradient(ellipse at center, #000428 0%, #004e92 35%, #001a3a 100%);
                background-attachment: fixed;
            }}
            .main-header, .score, .section-title, .balance-display, .current-bet, .bet-title, .split-hand-title {{
                color: #87CEEB;
            }}
            .player-section, .dealer-section {{
                border: 2px solid rgba(135, 206, 235, 0.3);
            }}
            .bet-section {{
                background: rgba(135, 206, 235, 0.2);
                border: 2px solid #87CEEB;
            }}
            .stats-container, .sidebar-info, .theme-selector {{
                border: 1px solid rgba(135, 206, 235, 0.3);
                color: #87CEEB;
            }}
            .active-hand {{
                border: 3px solid #87CEEB !important;
            }}
            {base_styles}
        </style>"""

    else:
        return get_theme_css("Classic Green")


class BlackjackGame:
    def __init__(self):
        self.suits = ['♠', '♥', '♦', '♣']
        self.ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.deck = []
        self.balance = 5000
        self.current_bet = 0
        self.bet_placed = False
        self.has_doubled = False
        self.has_split = False
        self.split_hands = []
        self.active_hand = 0
        self.reset_game()

    def create_deck(self):
        self.deck = [(rank, suit) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.deck)

    def deal_card(self):
        if len(self.deck) < 10:
            self.create_deck()
        return self.deck.pop()

    def calculate_hand_value(self, hand: List[Tuple[str, str]]) -> int:
        value = 0
        aces = 0

        for rank, _ in hand:
            if rank in ['J', 'Q', 'K']:
                value += 10
            elif rank == 'A':
                aces += 1
                value += 11
            else:
                value += int(rank)

        while value > 21 and aces > 0:
            value -= 10
            aces -= 1

        return value

    def reset_game(self):
        self.create_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.game_over = False
        self.player_stood = False
        self.game_result = ""
        self.bet_placed = False
        self.current_bet = 0
        self.has_doubled = False
        self.has_split = False
        self.split_hands = []
        self.active_hand = 0

    def place_bet(self, amount: int):
        if 50 <= amount <= 1000 and amount <= self.balance:
            self.current_bet = amount
            self.bet_placed = True
            return True
        return False

    def has_blackjack(self, hand):
        if len(hand) != 2:
            return False

        ranks = [card[0] for card in hand]
        has_ace = 'A' in ranks
        has_ten_value = any(rank in ['10', 'J', 'Q', 'K'] for rank in ranks)

        return has_ace and has_ten_value

    def deal_initial_cards(self):
        self.player_hand = [self.deal_card(), self.deal_card()]
        self.dealer_hand = [self.deal_card(), self.deal_card()]

        player_bj = self.has_blackjack(self.player_hand)
        dealer_bj = self.has_blackjack(self.dealer_hand)

        if player_bj or dealer_bj:
            self.game_over = True

            if player_bj and dealer_bj:
                self.game_result = "push_blackjack"
            elif player_bj:
                self.game_result = "player_blackjack"
                winnings = int(self.current_bet * 1.5)
                self.balance += winnings
            else:
                self.game_result = "dealer_blackjack"
                self.balance -= self.current_bet

    def can_double_down(self):
        if self.has_split:
            current_hand = self.split_hands[self.active_hand]
            return len(current_hand) == 2 and not self.has_doubled and self.balance >= self.current_bet
        else:
            return len(self.player_hand) == 2 and not self.has_doubled and self.balance >= self.current_bet

    def can_split(self):
        if self.has_split or len(self.player_hand) != 2:
            return False
        card1_value = self.get_card_value(self.player_hand[0][0])
        card2_value = self.get_card_value(self.player_hand[1][0])
        return card1_value == card2_value and self.balance >= self.current_bet

    def get_card_value(self, rank):
        if rank in ['J', 'Q', 'K']:
            return 10
        elif rank == 'A':
            return 11
        else:
            return int(rank)

    def double_down(self):
        if self.can_double_down():
            self.balance -= self.current_bet
            self.current_bet *= 2
            self.has_doubled = True

            if self.has_split:
                self.split_hands[self.active_hand].append(self.deal_card())
                if self.calculate_hand_value(self.split_hands[self.active_hand]) > 21:
                    self.check_split_hand_completion()
                else:
                    self.check_split_hand_completion()
            else:
                self.player_hand.append(self.deal_card())
                if self.calculate_hand_value(self.player_hand) > 21:
                    self.game_over = True
                    self.game_result = "bust"
                    self.balance -= self.current_bet
                else:
                    self.player_stand()
            return True
        return False

    def split_hand(self):
        if self.can_split():
            self.balance -= self.current_bet
            self.has_split = True

            card1 = self.player_hand[0]
            card2 = self.player_hand[1]

            self.split_hands = [[card1], [card2]]
            self.player_hand = []
            self.active_hand = 0

            self.split_hands[0].append(self.deal_card())
            self.split_hands[1].append(self.deal_card())

            return True
        return False

    def get_current_hand(self):
        if self.has_split:
            return self.split_hands[self.active_hand]
        else:
            return self.player_hand

    def check_split_hand_completion(self):
        if self.has_split:
            if self.active_hand == 0:
                self.active_hand = 1
                self.has_doubled = False
            else:
                self.player_stood = True
                self.dealer_play()
        else:
            self.player_stand()

    def player_hit(self):
        if not self.game_over:
            current_hand = self.get_current_hand()
            current_hand.append(self.deal_card())

            if self.calculate_hand_value(current_hand) > 21:
                if self.has_split:
                    self.check_split_hand_completion()
                else:
                    self.game_over = True
                    self.game_result = "bust"
                    self.balance -= self.current_bet

    def player_stand(self):
        if self.has_split:
            self.check_split_hand_completion()
        else:
            self.player_stood = True
            self.dealer_play()

    def dealer_play(self):
        time.sleep(0.8)

        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deal_card())
            if self.calculate_hand_value(self.dealer_hand) < 17:
                time.sleep(0.4)

        self.game_over = True
        self.determine_winner()

    def determine_winner(self):
        dealer_value = self.calculate_hand_value(self.dealer_hand)

        if self.has_split:
            total_winnings = 0
            wins = 0
            losses = 0
            pushes = 0

            for i, hand in enumerate(self.split_hands):
                hand_value = self.calculate_hand_value(hand)
                bet_amount = self.current_bet // 2

                if hand_value > 21:
                    losses += 1
                elif dealer_value > 21:
                    total_winnings += bet_amount
                    wins += 1
                elif hand_value > dealer_value:
                    total_winnings += bet_amount
                    wins += 1
                elif hand_value < dealer_value:
                    total_winnings -= bet_amount
                    losses += 1
                else:
                    pushes += 1

            self.balance += total_winnings

            if wins > losses:
                self.game_result = "win"
            elif losses > wins:
                self.game_result = "lose"
            else:
                self.game_result = "push"
        else:
            player_value = self.calculate_hand_value(self.player_hand)

            if player_value > 21:
                self.game_result = "bust"
                self.balance -= self.current_bet
            elif dealer_value > 21:
                self.game_result = "dealer_bust"
                self.balance += self.current_bet
            elif player_value > dealer_value:
                self.game_result = "win"
                self.balance += self.current_bet
            elif player_value < dealer_value:
                self.game_result = "lose"
                self.balance -= self.current_bet
            else:
                self.game_result = "push"


def display_hand(hand: List[Tuple[str, str]], hide_first: bool = False, title: str = "") -> str:
    cards_html = '<div class="cards-container">'
    if title:
        cards_html = f'<div class="split-hand-title">{title}</div><div class="cards-container">'

    for i, (rank, suit) in enumerate(hand):
        if hide_first and i == 0:
            cards_html += '<div class="card">🂠</div>'
        else:
            color_class = "card-red" if suit in ['♥', '♦'] else "card-black"
            cards_html += f'<div class="card {color_class}">{rank}{suit}</div>'
    cards_html += '</div>'
    return cards_html


# Initialize theme and game
if 'theme' not in st.session_state:
    st.session_state.theme = "Classic Green"

if 'game' not in st.session_state:
    st.session_state.game = BlackjackGame()
    st.session_state.stats = {'wins': 0, 'losses': 0, 'pushes': 0, 'total_winnings': 0}

# Apply theme CSS
st.markdown(get_theme_css(st.session_state.theme), unsafe_allow_html=True)

game = st.session_state.game

# Main layout with sidebar
left_col, main_col = st.columns([1, 2])

with left_col:
    st.markdown('<h1 class="main-header">🃏 BLACKJACK 🃏</h1>', unsafe_allow_html=True)

    st.markdown(f'<div class="balance-display">💰 ${game.balance:,}</div>', unsafe_allow_html=True)

    st.markdown('<div class="theme-selector">', unsafe_allow_html=True)
    st.markdown("**🎨 Choose Theme**")
    theme_options = ["Classic Green", "Vegas Gold", "Royal Purple", "Midnight Blue"]

    if st.session_state.theme not in theme_options:
        st.session_state.theme = "Classic Green"

    selected_theme = st.selectbox("", theme_options, index=theme_options.index(st.session_state.theme),
                                  key="theme_select", label_visibility="collapsed")

    if selected_theme != st.session_state.theme:
        st.session_state.theme = selected_theme
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 🎮 Game Controls")
    if st.button("🎮 New Game", key="new_game", use_container_width=True):
        st.session_state.game.reset_game()
        st.rerun()

    if st.button("💰 Reset Balance", key="reset_balance", use_container_width=True):
        st.session_state.game.balance = 5000
        st.session_state.game.reset_game()
        st.rerun()

    if st.button("📊 Reset Stats", key="reset_stats", use_container_width=True):
        st.session_state.stats = {'wins': 0, 'losses': 0, 'pushes': 0, 'total_winnings': 0}
        st.rerun()

    st.markdown('<div class="sidebar-info">', unsafe_allow_html=True)
    st.markdown("**📈 STATS**")
    stats = st.session_state.stats
    total_games = stats['wins'] + stats['losses'] + stats['pushes']
    if total_games > 0:
        win_rate = (stats['wins'] / total_games) * 100
        st.markdown(f"**Games:** {total_games}")
        st.markdown(f"**W:** {stats['wins']} **L:** {stats['losses']} **P:** {stats['pushes']}")
        st.markdown(f"**Win Rate:** {win_rate:.0f}%")

        total_winnings = stats['total_winnings']
        color = "#32CD32" if total_winnings >= 0 else "#FF6B6B"
        symbol = "📈" if total_winnings >= 0 else "📉"
        st.markdown(f"**Net:** <span style='color: {color};'>{symbol} ${total_winnings:,}</span>",
                    unsafe_allow_html=True)
    else:
        st.markdown("Ready to play!")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-info">', unsafe_allow_html=True)
    st.markdown("**🎯 How to Play**")
    st.markdown("""
    **Goal:** Get close to 21 without going over!

    **Card Values:**
    - 2-10: Face value
    - J, Q, K: 10 points  
    - Ace: 1 or 11

    **Rules:**
    - Dealer hits on 16 or less
    - Dealer stands on 17+
    - Over 21 = Bust (lose)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with main_col:
    if not game.bet_placed and not game.game_over:
        st.markdown('<div class="bet-section">', unsafe_allow_html=True)
        st.markdown('<div class="bet-title">🎰 PLACE BET</div>', unsafe_allow_html=True)
        st.markdown('<div class="bet-subtitle">Min: $50 • Max: $1,000</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            if st.button("$50", key="bet_50", use_container_width=True):
                if game.place_bet(50):
                    st.rerun()
            if st.button("$250", key="bet_250", use_container_width=True):
                if game.place_bet(250):
                    st.rerun()

        with col2:
            if st.button("$100", key="bet_100", use_container_width=True):
                if game.place_bet(100):
                    st.rerun()
            if st.button("$500", key="bet_500", use_container_width=True):
                if game.place_bet(500):
                    st.rerun()

        custom_bet = st.number_input("Custom Amount", min_value=50, max_value=min(1000, game.balance), step=50,
                                     key="custom_bet")
        if st.button("PLACE BET", key="place_custom", use_container_width=True):
            if game.place_bet(custom_bet):
                st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

        if not game.bet_placed:
            st.stop()
    else:
        if game.current_bet > 0:
            st.markdown(f'<div class="current-bet">Current Bet: ${game.current_bet}</div>', unsafe_allow_html=True)

    if game.bet_placed and not game.player_hand and not game.dealer_hand:
        game.deal_initial_cards()

    st.markdown('<div class="dealer-section">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎩 DEALER</div>', unsafe_allow_html=True)
    if game.game_over or game.player_stood:
        dealer_cards = display_hand(game.dealer_hand)
        dealer_value = game.calculate_hand_value(game.dealer_hand)
        st.markdown(f'<div class="score">Value: {dealer_value}</div>', unsafe_allow_html=True)
    else:
        dealer_cards = display_hand(game.dealer_hand, hide_first=True)
        st.markdown('<div class="score">Value: ?</div>', unsafe_allow_html=True)

    st.markdown(dealer_cards, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if game.has_split:
        for i, hand in enumerate(game.split_hands):
            section_class = "player-section"
            if i == game.active_hand and not game.game_over:
                section_class += " active-hand"

            st.markdown(f'<div class="{section_class}">', unsafe_allow_html=True)
            hand_title = f"🎯 HAND {i + 1}"
            if i == game.active_hand and not game.game_over:
                hand_title += " (ACTIVE)"
            st.markdown(f'<div class="section-title">{hand_title}</div>', unsafe_allow_html=True)

            hand_value = game.calculate_hand_value(hand)
            st.markdown(f'<div class="score">Value: {hand_value}</div>', unsafe_allow_html=True)

            player_cards = display_hand(hand)
            st.markdown(player_cards, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="player-section">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🎯 PLAYER</div>', unsafe_allow_html=True)
        player_cards = display_hand(game.player_hand)
        player_value = game.calculate_hand_value(game.player_hand)
        st.markdown(f'<div class="score">Value: {player_value}</div>', unsafe_allow_html=True)
        st.markdown(player_cards, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if not game.game_over and not game.player_stood:
        if game.player_hand or game.has_split:
            st.markdown('<div class="game-action-buttons">', unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            with col1:
                if st.button("🃏 HIT", key="hit", use_container_width=True):
                    game.player_hit()
                    st.rerun()

            with col2:
                if st.button("✋ STAND", key="stand", use_container_width=True):
                    game.player_stand()
                    st.rerun()

            col3, col4 = st.columns(2)

            with col3:
                if game.can_double_down():
                    if st.button(f"⬆️ DOUBLE (${game.current_bet})", key="double", use_container_width=True):
                        game.double_down()
                        st.rerun()

            with col4:
                if game.can_split():
                    if st.button(f"✂️ SPLIT (${game.current_bet})", key="split", use_container_width=True):
                        game.split_hand()
                        st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)

    elif game.player_stood and not game.game_over:
        st.markdown(
            '<div style="text-align: center; color: #FFD700; font-size: 1.3rem; margin: 20px 0;">🎴 Dealer playing...</div>',
            unsafe_allow_html=True)

    if game.game_over:
        if game.game_result == "player_blackjack":
            st.markdown('<div class="win-message">🎉 BLACKJACK! 🎉</div>', unsafe_allow_html=True)
            winnings = int(game.current_bet * 1.5)
            st.markdown(
                f'<div style="text-align: center; color: #32CD32; font-size: 1.2rem;">21! +${winnings} (3:2 payout)</div>',
                unsafe_allow_html=True)
            st.session_state.stats['wins'] += 1
            st.session_state.stats['total_winnings'] += winnings
        elif game.game_result == "dealer_blackjack":
            st.markdown('<div class="lose-message">💔 DEALER BLACKJACK</div>', unsafe_allow_html=True)
            st.markdown(f'<div style="text-align: center; color: #FF6B6B;">Dealer 21! -${game.current_bet}</div>',
                        unsafe_allow_html=True)
            st.session_state.stats['losses'] += 1
            st.session_state.stats['total_winnings'] -= game.current_bet
        elif game.game_result == "push_blackjack":
            st.markdown(
                '<div style="font-size: 1.5rem; font-weight: bold; color: #FFA500; text-align: center;">🤝 BOTH BLACKJACK!</div>',
                unsafe_allow_html=True)
            st.markdown(f'<div style="text-align: center; color: #FFA500;">Push! +$0</div>', unsafe_allow_html=True)
            st.session_state.stats['pushes'] += 1
        elif game.game_result == "bust":
            st.markdown('<div class="lose-message">💥 BUST!</div>', unsafe_allow_html=True)
            st.markdown(f'<div style="text-align: center; color: #FF6B6B;">-${game.current_bet}</div>',
                        unsafe_allow_html=True)
            st.session_state.stats['losses'] += 1
            st.session_state.stats['total_winnings'] -= game.current_bet
        elif game.game_result == "dealer_bust":
            st.markdown('<div class="win-message">🎉 DEALER BUSTS!</div>', unsafe_allow_html=True)
            st.markdown(f'<div style="text-align: center; color: #32CD32;">+${game.current_bet}</div>',
                        unsafe_allow_html=True)
            st.session_state.stats['wins'] += 1
            st.session_state.stats['total_winnings'] += game.current_bet
        elif game.game_result == "win":
            st.markdown('<div class="win-message">🎉 YOU WIN!</div>', unsafe_allow_html=True)
            st.markdown(f'<div style="text-align: center; color: #32CD32;">+${game.current_bet}</div>',
                        unsafe_allow_html=True)
            st.session_state.stats['wins'] += 1
            st.session_state.stats['total_winnings'] += game.current_bet
        elif game.game_result == "lose":
            st.markdown('<div class="lose-message">😞 YOU LOSE</div>', unsafe_allow_html=True)
            st.markdown(f'<div style="text-align: center; color: #FF6B6B;">-${game.current_bet}</div>',
                        unsafe_allow_html=True)
            st.session_state.stats['losses'] += 1
            st.session_state.stats['total_winnings'] -= game.current_bet
        elif game.game_result == "push":
            st.markdown(
                '<div style="font-size: 1.5rem; font-weight: bold; color: #FFA500; text-align: center;">🤝 PUSH!</div>',
                unsafe_allow_html=True)
            st.markdown(f'<div style="text-align: center; color: #FFA500;">+$0</div>', unsafe_allow_html=True)
            st.session_state.stats['pushes'] += 1

        if game.balance < 50:
            st.markdown(
                '<div style="font-size: 1.8rem; font-weight: bold; color: #FF0000; text-align: center; animation: pulse 2s infinite;">💸 BANKRUPT! 💸</div>',
                unsafe_allow_html=True)

        st.markdown('<div class="game-action-buttons">', unsafe_allow_html=True)
        if st.button("🎮 DEAL NEW HAND", key="new_hand", use_container_width=True):
            st.session_state.game.reset_game()
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

if game.player_stood and not game.game_over:
    time.sleep(0.3)
    st.rerun()