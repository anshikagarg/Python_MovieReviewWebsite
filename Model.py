import Media
import fresh_tomatoes


sucide_squad = Media.Movie("Sucide Squad", "It is Bad v Evil", "poster_image/suicideSquad.png", "https://www.youtube.com/watch?v=CmRih_VtVAs")

mad_max = Media.Movie("Mad Max: Fury Road", "A woman rebels against a tyrannical ruler in postapocalyptic Australia", "poster_image/madMax.jpg", 
"https://www.youtube.com/watch?v=hEJnMQG9ev8")

finding_dory = Media.Movie("Finding Dory", "The friendly but forgetful blue tang fish begins a search for her long-lost parents.", 
"poster_image/findingDory.jpg", "https://www.youtube.com/watch?v=UGWv91YZua4")

jungle_book = Media.Movie("The Jungle Book", "After a threat from the tiger Shere Khan forces him to flee the jungle, a man-cub named Mowgli embarks on a journey of self discovery with the help of panther, Bagheera, and free spirited bear, Baloo.", 
"poster_image/jungleBook.jpeg", "https://www.youtube.com/watch?v=WtR9tqPa48s")

Movies = [sucide_squad, mad_max, finding_dory, jungle_book]

fresh_tomatoes.open_movies_page(Movies)

