# poker

[200~中文版

一副扑克有52张牌，每张牌由一个花色和一个数字构成。

花色为以下四者之一：

方片 D
黑桃 S
红桃 H
梅花 C

数字为以下13者之一，且大小顺序如下：

2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A

花色是大小无序的，但数字有序，2最小，A最大。

一手牌有5张。根据花色和数字的不同，其大小按照以下规则决定。

满足下面规则的手牌会大于满足上面规则的手牌。

同花顺＞铁支＞葫芦＞同花＞顺子＞三条＞两对＞对子＞散牌

    散牌：

        不符合其他任何规则的五张牌。 比较最大一张牌的大小，如果相同，比较第二大的牌的牌点数，如果五张牌的牌点数都相同，则为平局。

	    对子：

	        有两张同样大小的牌片。 比较两张大小一样的牌的牌点数，如果相同，依次比较剩余的三张牌大小。若大小都相同，则为平局。

		    两对：

		        有两个对子牌。 比较大对子的大小，若相同，比较小对子的大小，若还相同，比较单张牌的大小，若还相同，则为平局。

			    三条：

			        有三张同样大小的牌片。 比较三张大小一样的牌的牌点数大小。

				    顺子：

				        五张相连的牌。 比较最大的牌点数。若大小都相同，则为平局。

					    同花：

					        五张牌的花色相同。 按照散排规则比较大小。

						    葫芦：

						        三条+对子。 比较三张大小一样的牌的牌点数。

							    铁支：

							        有四张同样大小的牌片。 比较四张大小一样的牌的牌点数。

								    同花顺：

								        同一种花色的顺子。 比较最大的牌的牌的大小。若大小都相同，则为平局。

									你的工作是为两手牌判断大小。

									例如：

									输入: Black: 2H 3D 5S 9C KD White: 2C 3H 4S 8C AH 输出: White wins - high card: Ace

									输入: Black: 2H 4S 4C 2D 4H White: 2S 8S AS QS 3S 输出: Black wins - full house

									输入: Black: 2H 3D 5S 9C KD White: 2C 3H 4S 8C KH 输出: Black wins - high card: 9

									输入: Black: 2H 3D 5S 9C KD White: 2D 3H 5C 9S KH 输出: Tie
									English version

									A poker deck contains 52 cards - each card has a suit which is one of clubs, diamonds, hearts, or spades (denoted C, D, H, and S in the input data).

									Each card also has a value which is one of 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, ace (denoted 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A).

									For scoring purposes, the suits are unordered while the values are ordered as given above, with 2 being the lowest and ace the highest value.

									A poker hand consists of 5 cards dealt from the deck. Poker hands are ranked by the following partial order from lowest to highest.

									High Card: Hands which do not fit any higher category are ranked by the value of their highest card. If the highest cards have the same value, the hands are ranked by the next highest, and so on.

									Pair: 2 of the 5 cards in the hand have the same value. Hands which both contain a pair are ranked by the value of the cards forming the pair. If these values are the same, the hands are ranked by the values of the cards not forming the pair, in decreasing order.

									Two Pairs: The hand contains 2 different pairs. Hands which both contain 2 pairs are ranked by the value of their highest pair. Hands with the same highest pair are ranked by the value of their other pair. If these values are the same the hands are ranked by the value of the remaining card.

									Three of a Kind: Three of the cards in the hand have the same value. Hands which both contain three of a kind are ranked by the value of the 3 cards.

									Straight: Hand contains 5 cards with consecutive values. Hands which both contain a straight are ranked by their highest card.

									Flush: Hand contains 5 cards of the same suit. Hands which are both flushes are ranked using the rules for High Card.

									Full House: 3 cards of the same value, with the remaining 2 cards forming a pair. Ranked by the value of the 3 cards.

									Four of a kind: 4 cards with the same value. Ranked by the value of the 4 cards.

									Straight flush: 5 cards of the same suit with consecutive values. Ranked by the highest card in the hand.

									Your job is to rank pairs of poker hands and to indicate which, if either, has a higher rank.

									Examples:

									Input: Black: 2H 3D 5S 9C KD White: 2C 3H 4S 8C AH Output: White wins - high card: Ace

									Input: Black: 2H 4S 4C 2D 4H White: 2S 8S AS QS 3S Output: Black wins - full house

									Input: Black: 2H 3D 5S 9C KD White: 2C 3H 4S 8C KH Output: Black wins - high card: 9

									Input: Black: 2H 3D 5S 9C KD White: 2D 3H 5C 9S KH Output: Tie
