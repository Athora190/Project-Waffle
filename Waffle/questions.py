from questions_model import Questions

def seed_data():
    a_key = Questions(question="Who has the most rings in the NBA?",
                        choice1 ="Kobe Bryant",
                        choice2 ="Michael Jordan",
                        choice3 ="Bill Russel",
                        choice4 ="Lebron James",
                        correct_answer ="Bill Russel",
                        ).put()

    b_key = Questions(question="Who is the only athlete ever to play in a Super Bowl and a World Series?",
                        choice1 ="Peyton Manning",
                        choice2 ="Deion Sanders",
                        choice3 ="Tom Brady",
                        choice4 ="Donald Trump",
                        correct_answer ="Deion Sanders",
                        ).put()

    c_key = Questions(question="What is the regulation height for a basketball hoop?",
                        choice1 ="8 feet",
                        choice2 ="12 feet",
                        choice3 ="5 feet",
                        choice4 ="10 feet",
                        correct_answer ="10 feet",
                        ).put()

    d_key = Questions(question="How many stars are in the sky?",
                        choice1 ="5 billion",
                        choice2 ="3 thousand",
                        choice3 ="10 billion",
                        choice4 ="there are too many to count",
                        correct_answer ="there are too many to count",
                        ).put()

    e_key = Questions(question="How many types of stars are there?",
                        choice1 ="3",
                        choice2 ="5",
                        choice3 ="12",
                        choice4 ="80",
                        correct_answer ="5",
                        ).put()

    f_key = Questions(question="Who is Simba's father?",
                        choice1 ="Mufasa",
                        choice2 ="Scar",
                        choice3 ="Wreak it Ralph",
                        choice4 ="Sitka",
                        correct_answer ="Mufasa",
                        ).put()

    g_key = Questions(question="How many soccer players should be on the field at the same time?",
                        choice1 ="22",
                        choice2 ="20",
                        choice3 ="15",
                        choice4 ="17",
                        correct_answer ="22",
                        ).put()

    h_key = Questions(question="What NFL Quarterback has been in the most Super Bowls?",
                        choice1 ="Joe Montana",
                        choice2 ="Tom Brady",
                        choice3 ="Eli Manning",
                        choice4 ="Peyton Manning",
                        correct_answer ="Tom Brady",
                        ).put()

    i_key = Questions(question="Who was the first black baseball player to play in the major leagues?",
                        choice1 ="Derek Jeter",
                        choice2 ="Jackie Robinson",
                        choice3 ="Michael Jordan",
                        choice4 ="Babe Ruth",
                        correct_answer ="Jackie Robinson",
                        ).put()

    j_key = Questions(question="Who broke the record for the fastest man alive in the 2008 Summer Olympics?",
                        choice1 ="Usain Bolt",
                        choice2 ="Tyreek Hill",
                        choice3 ="Tyson Gay",
                        choice4 ="Chris Johnson",
                        correct_answer ="Usain Bolt",
                        ).put()

    k_key = Questions(question="How many gold medals does Michael Phelps have?",
                        choice1 ="28",
                        choice2 ="25",
                        choice3 ="23",
                        choice4 ="27",
                        correct_answer ="23",
                        ).put()

    l_key = Questions(question="How many total bases are there on a baseball field?",
                        choice1 ="1",
                        choice2 ="5",
                        choice3 ="4",
                        choice4 ="3",
                        correct_answer ="4",
                        ).put()

    m_key = Questions(question="Which is the least popular sport in the World?",
                        choice1 ="Soccer",
                        choice2 ="Cricket",
                        choice3 ="Volleyball",
                        choice4 ="Basketball",
                        correct_answer ="Basketball",
                        ).put()

    n_key = Questions(question="Who was the only President to serve more than two terms?",
                        choice1 ="Franklin D Roosevelt",
                        choice2 ="George Washington",
                        choice3 ="Ulysses S. Grant",
                        choice4 ="Theodore Roosevelt",
                        correct_answer ="Franklin D Roosevelt",
                        ).put()

    o_key = Questions(question="Who was the only President to serve two non-consecutive terms?",
                        choice1 ="Grover Cleveland",
                        choice2 ="Theodore Roosevelt",
                        choice3 ="Woodrow Wilson",
                        choice4 ="Ronald Reagan",
                        correct_answer ="Grover Cleveland",
                        ).put()

    p_key = Questions(question="Who was the oldest elected President?",
                        choice1 ="Donald Trump",
                        choice2 ="Dwight D. Eisenhower",
                        choice3 ="Ronald Reagan",
                        choice4 ="James Buchanan",
                        correct_answer ="Ronald Reagan",
                        ).put()

    q_key = Questions(question="Who was the first President to live in the White House?",
                        choice1 ="John Adams",
                        choice2 ="Thomas Jefferson",
                        choice3 ="Andrew Jackson",
                        choice4 ="George Washington",
                        correct_answer ="John Adams",
                        ).put()

    r_key = Questions(question="Who was the first President born outside the contiguous United States?",
                        choice1 ="William Howard Taft",
                        choice2 ="Barack Obama",
                        choice3 ="Benjamin Harrison",
                        choice4 ="Franklin Pierce",
                        correct_answer ="Barack Obama",
                        ).put()

    s_key = Questions(question="What American president is associated with the Teddy Bear?",
                        choice1 ="Richard Nixon",
                        choice2 ="Woodrow Wilson",
                        choice3 ="Ted Kennedy",
                        choice4 ="Theodore Roosevelt",
                        correct_answer ="Theodore Roosevelt",
                        ).put()

    t_key = Questions(question="Which U.S. President signed the treaty to purchase Alaska from Russia?",
                        choice1 ="Andrew Johnson",
                        choice2 ="James Buchanan",
                        choice3 ="Andrew Jackson",
                        choice4 ="Ulysses S. Grant",
                        correct_answer ="Andrew Johnson",
                        ).put()

    u_key = Questions(question="Who was the first President to appear on TV?",
                        choice1 ="Harry S. Truman",
                        choice2 ="Franklin D. Roosevelt",
                        choice3 ="Dwight D. Eisenhower",
                        choice4 ="John F. Kennedy",
                        correct_answer ="Franklin D. Roosevelt",
                        ).put()

    v_key = Questions(question="Who was the first President to be impeached?",
                        choice1 ="Richard Nixon",
                        choice2 ="Andrew Johnson",
                        choice3 ="Bill Clinton",
                        choice4 ="Calvin Coolidge",
                        correct_answer ="Andrew Johnson",
                        ).put()

    w_key = Questions(question="Who was the only unanimously elected President by the Electoral College?",
                        choice1 ="Franklin D Roosevelt",
                        choice2 ="George Washington",
                        choice3 ="John F. Kennedy",
                        choice4 ="Ronald Reagan",
                        correct_answer ="George Washington",
                        ).put()

    z_key = Questions(question="How did Cinderalla lose her glass slipper?",
                        choice1 ="she gave it away.",
                        choice2 ="she never had a glass slipper.",
                        choice3 ="she ran and it fell off her foot.",
                        choice4 ="Someone stole it.",
                        correct_answer ="she ran and it fell off her foot.",
                        ).put()

    y_key = Questions(question="Why did Mulan join the military?",
                        choice1 ="she wanted to prove that she can fight like a man.",
                        choice2 ="Restore honor to her family's name.",
                        choice3 ="To fall in love with a soldier.",
                        choice4 ="To run away from her family.",
                        correct_answer ="Restore honor to her family's name.",
                        ).put()

    z_key = Questions(question="How did Hiccup lose a leg?",
                        choice1 ="He was born without one",
                        choice2 ="He lost it by trying to save toothless.",
                        choice3 ="It got cut off because he disrespected his father.",
                        choice4 ="It broke off of his leg",
                        correct_answer ="He lost it by trying to save toothless.",
                        ).put()

    ab_key = Questions(question="What is the biggest plant in our solor system?",
                        choice1 ="Jupiter",
                        choice2 ="Saturn",
                        choice3 ="Pluto",
                        choice4 ="The Sun",
                        correct_answer ="Jupiter",
                        ).put()

    cd_key = Questions(question="What happends when a super giant explodes?",
                        choice1 ="becomes a dead star",
                        choice2 ="becomes a black hole",
                        choice3 ="nothing happends",
                        choice4 ="both a and b",
                        correct_answer ="both a and b",
                        ).put()

    ef_key = Questions(question="how big is the milky way galaxy in light years?",
                        choice1 ="20,000",
                        choice2 ="100,000",
                        choice3 ="500,000",
                        choice4 ="no on knows",
                        correct_answer ="100,000",
                        ).put()

    gh_key = Questions(question="Why did Kenai kill Koda's mom?",
                        choice1 ="She tried to kill him.",
                        choice2 ="He didn't kill Koda's mom.",
                        choice3 ="She killed Denahi",
                        choice4 ="Kenai killed her by accident.",
                        correct_answer ="She killed Denahi",
                        ).put()
