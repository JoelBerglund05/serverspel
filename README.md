# serverspel Loggbok

## vecka 46

När jag arbetade hemma och committa till github upptäckte jag efter att jag hade glömt committa saker från skoldatorn vilket gjorde att vissa saker ser anurlunda ut än vad det gjorde så nu när du connectar kommer inte.

    http://127.0.0.1:5000/game?game_token=<game_token>

utan det kommer

    http://127.0.0.1:5000/game/<game_token>

det verkar funka bra så jag låter det vara så tills vidare.

## vecka 45

Jag fortsatte på det jag höll på med förra veckan men jag lyckades bygga färdigt det ganska
fort. jag började då med att bygga en sida där jag kunnde lista all aktiva games som du har
startat. Detta var mycket svårare än jag trodde jag hittade massor av sett som jag kunnde
bygga det men nästan alla var inte "scalible" eller alldeles för kompliserade för att börja
med att köra på men till sisst hittade jag att jag kunde lägga in min game token på detta
sätt:

    http://127.0.0.1:5000/game?game_token=<game_token>

och sen checka min tiken
och validera den för att sen kunna ge användaren en fråga. jag hittade lösningen genom att
fråga bings chatt bot: how could i set up my html document to have a link with the token as
url in flask?

    http://yourgame.com/special-feature?token=<game_token>
    how could i get the token so i can vaslidate it?

svaret på första frågan:

    <a href="{{ url_for('special_game', token=token) }}">Play Special Game</a>

svaret på andra frågan:

    game_token = request.args.get('token')

## vecka 44

Jag började bygga ett authentication system och jag insåg att flask använder sig av coockies för att kolla om perosnen är inloggad vilket gjorde att jag valde att bygga frågesports spelet med en webbsida som visar allt. jag har också hunnit skapa en "game session" så du kan skapa en request av ett spel med en annan spelare men också kunna gå med i ett spel om en sådan request redan har skapats.

## vecka 43

Jag började med att skapa servern och clienten. de svåra var att få servern att svara clienten via en print() men de var mycket lättare än jag förväntade mig.

## vecka 42

Jag Startade projectet och tittade på hu jag ville göra projectet. jag började med att försöka bygga servern från grunden upp men insåg att det skulle bli för mycket arbete så jag kom fram till att jag bygger projectet i flask vilket är ett biblotek för python.
