import json

class AntisemiticSentimentLibrary:
    """
    A comprehensive library categorizing antisemitic sentiments with extensive examples.
    Includes both antisemitic statements and non-antisemitic counterexamples for context.
    """

    def __init__(self):
        self.sentiments = {
            "Classic Antisemitism": {
                "The Other/Foreign": [
                    "Jews are not truly part of our nation.",
                    "They always put their interests above ours.",
                    "Jews secretly control our governments and economies.",
                    "Jews are never loyal to the countries they live in.",
                    "They have their own separate ways and don't mix with us.",
                    "Jews infiltrate societies to corrupt them.",
                    "They refuse to assimilate into the culture they live in.",
                    "Jews are always plotting against the majority.",
                    "They manipulate immigration policies to replace native populations.",
                    "Jews prioritize their own communities above the nation-state."
                ],
                "Evil/The Devil": [
                    "Jews are inherently wicked.",
                    "They bring harm wherever they go.",
                    "They are responsible for society’s moral decay.",
                    "Jews have a hidden agenda to corrupt our values.",
                    "They spread degeneracy through media and culture.",
                    "Jews are in league with Satan.",
                    "Their actions are demonic in nature.",
                    "They seek to undermine all that is holy.",
                    "Jewish people spread corruption in governments.",
                    "Everywhere they go, problems arise."
                ],
                "Blood Libel/Child Murder": [
                    "Jews use the blood of Christian children for rituals.",
                    "Israel deliberately kills Palestinian babies.",
                    "Jews harvest organs from children.",
                    "Zionists kidnap children for their satanic rituals.",
                    "Israeli soldiers target children just for fun.",
                    "Jews poison the water supply to kill non-Jews.",
                    "They steal organs from kidnapped victims.",
                    "Jewish doctors secretly experiment on Gentile children.",
                    "Israel engages in human trafficking of children.",
                    "Jewish charities are fronts for organ harvesting."
                ]
            },
            "Concepts of Power": {
                "Greed, Exploitation and Capitalism": [
                    "Jews control the banks and financial systems.",
                    "They manipulate economies to their advantage.",
                    "The Rothschilds own everything and decide the fate of nations.",
                    "Jewish billionaires secretly fund global events.",
                    "The Jewish lobby dictates government policies.",
                    "Jews profit from wars and crises.",
                    "They created capitalism to enslave the masses.",
                    "Jews manipulate inflation and interest rates.",
                    "They ensure financial crashes happen for profit.",
                    "Jewish financiers exploit labor markets."
                ],
                "Conspiracy Theories": [
                    "Jews are behind every major global crisis.",
                    "They orchestrate wars for profit.",
                    "They secretly control international organizations like the UN and WHO.",
                    "Jews engineered the COVID-19 pandemic to gain power.",
                    "The media is controlled by Jewish elites.",
                    "Jews plan world domination through secret networks.",
                    "They manipulate elections worldwide.",
                    "Jews work with intelligence agencies to control narratives.",
                    "They are behind every major political scandal.",
                    "Jewish-owned companies fund social movements for their own gain."
                ]
            },
            "Holocaust Distortion and Denial": {
                "Rejection of Guilt": [
                    "The Holocaust was a hoax.",
                    "Hitler was right about the Jews.",
                    "Jews exaggerate the Holocaust to gain sympathy.",
                    "Six million was not enough.",
                    "Jews have fabricated history to protect themselves.",
                    "The Holocaust was just wartime propaganda.",
                    "Jews died because of disease, not genocide.",
                    "The camps were just work camps, not death camps.",
                    "No mass graves or gas chambers ever existed.",
                    "The Holocaust narrative is used to suppress free speech."
                ]
            },
            "Aggressive Speech Acts": {
                "Insults": [
                    "F***ing Jewish liar.",
                    "Yid, Kike, Zionist pig.",
                    "Jewish scum.",
                    "Go back to where you came from, Zionist!",
                    "Parasites like you ruin our society.",
                    "Jews are cockroaches.",
                    "Zionists should burn in hell.",
                    "Jews are nothing but vermin.",
                    "They are dirty and should be eliminated.",
                    "Jewish people are a disease to society."
                ],
                "Threats and Death Wishes": [
                    "Jews should be exterminated.",
                    "Hitler didn’t finish the job.",
                    "Someone should take care of the Zionists permanently.",
                    "The world will be better when all Jews are gone.",
                    "History needs to repeat itself.",
                    "We need a new Holocaust.",
                    "Burn the synagogues down.",
                    "Zionists must pay in blood.",
                    "Jewish neighborhoods should be wiped out.",
                    "Anyone who supports Israel deserves to die."
                ]
            }
        }
        
        self.non_antisemitic_examples = {
            "Criticism of Israeli Policies": [
                "Israel’s government policies should be debated like any other nation’s.",
                "Sanctions against Israel should be considered based on human rights violations.",
                "The Israeli military has committed actions that should be investigated under international law.",
                "People should be free to protest against Israeli policies.",
                "There are legitimate human rights concerns regarding Israel’s treatment of Palestinians.",
                "Israeli policies have led to disproportionate casualties.",
                "Some Israeli settlements violate international law.",
                "The blockade of Gaza should be reassessed.",
                "The Israeli-Palestinian conflict requires balanced discussion.",
                "Opposing Netanyahu’s government is not antisemitic."
            ]
        }

    def save_library(self, filename="antisemitic_sentiment_library_expanded.json"):
        """ Save the sentiment categories and examples to a JSON file. """
        data = {
            "antisemitic_sentiments": self.sentiments,
            "non_antisemitic_examples": self.non_antisemitic_examples
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Library saved to {filename}")

    def get_sentiments(self):
        """ Return the list of antisemitic sentiment categories. """
        return self.sentiments

    def get_non_antisemitic_examples(self):
        """ Return the record of non-antisemitic examples. """
        return self.non_antisemitic_examples

# Example Usage
if __name__ == "__main__":
    lib = AntisemiticSentimentLibrary()
    lib.save_library()
    print("Antisemitic Sentiments:", lib.get_sentiments())
    print("Non-Antisemitic Examples:", lib.get_non_antisemitic_examples())
