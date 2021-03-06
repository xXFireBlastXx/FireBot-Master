import discord
import asyncio
import random
client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print("ID:")
    print(client.user.id)
    print("Ready to use!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("!deposite 1"):
        await client.send_message(message.channel, random.choice(["Te Faltan 4 monedas! :8ball:",
                                                                  "No me engañes, te faltan 4 monedas :8ball:",
                                                                  "Me sobran monedas asi que te dire la respuesta, SI :8ball:",
                                                                  "Me sobran monedas asi que te dire la respuesta, NO :8ball:"]))

    elif message.content.startswith("!deposite 2"):
        await client.send_message(message.channel, random.choice(["Te Faltan 3 monedas! :8ball:",
                                                                  "No me engañes, te faltan 3 monedas :8ball:",
                                                                  "Me sobran monedas asi que te dire la respuesta, SI :8ball:",
                                                                  "Me sobran monedas asi que te dire la respuesta, NO :8ball:"]))

    elif message.content.startswith("!deposite 3"):
        await client.send_message(message.channel, random.choice(["Te Faltan 2 monedas! :8ball:",
                                                                  "No me engañes, te faltan 2 monedas :8ball:",
                                                                  "Me sobran monedas asi que te dire la respuesta, SI :8ball:",
                                                                  "Me sobran monedas asi que te dire la respuesta, NO :8ball:"]))

    elif message.content.startswith("!deposite 4"):
        await client.send_message(message.channel, random.choice(["Te Falta 1 moneda! :8ball:",
                                                                  "No me engañes, te falta 1 moneda :8ball:",
                                                                  "Me sobran monedas asi que te dire la respuesta, SI :8ball:",
                                                                  "Me sobran monedas asi que te dire la respuesta, NO :8ball:"]))

    elif message.content.startswith("!deposite 5"):
        await client.send_message(message.channel, random.choice(["Gracias por depositar las 5 monedas! PD: La respuesta es SI :8ball:",
                                                                  "Gracias por depositar las 5 monedas! PD: La respuesta es NO :8ball:",
                                                                  "Gracias por depositar las 5 monedas! PD: No se la respuesta :8ball:"]))

    elif message.content.startswith("!deposite 6"):
        await client.send_message(message.channel, random.choice(["No te voy a regresar cambio! EH! PD: La respuesta es SI :8ball:",
                                                                  "No te voy a regresar cambio! EH! PD: La respuesta es NO :8ball:",
                                                                  "No te voy a regresar cambio! EH! PD: No se la respuesta :8ball:"]))

    elif message.content.startswith("!deposite 7"):
        await client.send_message(message.channel, random.choice(["No te voy a regresar cambio! EH! PD: La respuesta es SI :8ball:",
                                                                  "No te voy a regresar cambio! EH! PD: La respuesta es NO :8ball:",
                                                                  "No te voy a regresar cambio! EH! PD: No se la respuesta :8ball:"]))

    elif message.content.startswith("!deposite 8"):
        await client.send_message(message.channel, random.choice(["No te voy a regresar cambio! EH! PD: La respuesta es SI :8ball:",
                                                                  "No te voy a regresar cambio! EH! PD: La respuesta es NO :8ball:",
                                                                  "No te voy a regresar cambio! EH! PD: No se la respuesta :8ball:"]))

    elif message.content.startswith("!deposite 9"):
        await client.send_message(message.channel, random.choice(["No te voy a regresar cambio! EH! PD: La respuesta es SI :8ball:",
                                                                  "No te voy a regresar cambio! EH! PD: La respuesta es NO :8ball:",
                                                                  "No te voy a regresar cambio! EH! PD: No se la respuesta :8ball:"]))

    elif message.content.startswith("!deposite 10"):
        await client.send_message(message.channel, random.choice(["No te voy a regresar cambio! EH! PD: La respuesta es SI :8ball:",
                                                                  "No te voy a regresar cambio! EH! PD: La respuesta es NO :8ball:",
                                                                  "No te voy a regresar cambio! EH! PD: No se la respuesta :8ball:"]))
                                  
    elif message.content.startswith("!8ball"):
        await client.send_message(message.channel, random.choice(["Nop :8ball:",
                                                                  "Yes :8ball:",
                                                                  "No estoy seguro... :8ball:",
                                                                  "Sin Duda alguna! :8ball:",
                                                                  "Puede ser... :8ball:",
                                                                  "50%/50% :8ball:",
                                                                  "Dudoso... Kappa :8ball:",
                                                                  "Tu sabes mejor que yo la respuesta :8ball:",
                                                                  "Las Rosas son rojas, las violetas moradas, Yo no se la respuesta :8ball:",
                                                                  "Emmm, MIRA UNA MOSCA! :8ball:",
                                                                  "Si kvron, ya dejame en paz! :8ball:",
                                                                  "No kvron, ya dejame en paz! :8ball:",
                                                                  "Kyc y dejame dormir :8ball:",
                                                                  "2 + 2 = 4, 3 + 3 = 6, Tu no sabes cual es mi feis :8ball:",
                                                                  "Mejor dime tu la respuesta :8ball:",
                                                                  "¿Te has preguntado sobre mis respuestas fuera de lugar?... :8ball:",
                                                                  "Esto dibuja una sonrisa en mi cara :8ball:",
                                                                  "No se de que hablas... :8ball:",
                                                                  "No tengo una respuesta clara todavia... :8ball:",
                                                                  "Ahora si que la tengo y es... SI :8ball:",
                                                                  "Ahora si que la tengo y es... NO :8ball:",
                                                                  "No lo se, estoy muy ocupado perdiendo tu tiempo :smile: :8ball:",
                                                                  "¿Por que me envias eso? Eww... :8ball:",
                                                                  "Viaje en el futuro y vi un millon de preguntas y solo en una respondo... SI :8ball:",
                                                                  "Viaje en el futuro y vi un millon de preguntas y solo en una respondo... NO :8ball:",
                                                                  "Mejor vete de aqui :8ball:",
                                                                  "Hasta que me respondas cuanto es (2/7)(7/389) + 2x^2y^2 ÷ 3 + 7(3.1416 ÷ 3)(6723.95734 ÷ 1236x^8z^2y^4) + 1 , Te dire la respuesta :smile: :8ball:",
                                                                  "Si Juan se llevo 10 manzanas pero le dio las 10 a su amigo pero llega su mejor amigo, ¿Que sucedera? :thinking: :8ball:",
                                                                  "Las rosas son ro... espera, eso ya lo habia dicho... :8ball:",
                                                                  "Mejor abrazame :8ball:",
                                                                  "A Jesus no le gusta esto :8ball:",
                                                                  "A Jesus le gusta esto :8ball:",
                                                                  "No se a que te refieres con eso... :8ball:",
                                                                  "No se muy bien tu respuesta, tal vez la respuesta es SI :8ball:",
                                                                  "No se muy bien tu respuesta, tal vez la respuesta es NO :8ball:",
                                                                  "No se la respuesta pero deja de usar el pacman pls :8ball:",
                                                                  "Por favor deposite 5 monedas para obtener la respuesta :8ball:",
                                                                  "75%/25% :8ball:",
                                                                  "Si :8ball:",
                                                                  "No :8ball:",
                                                                  "La respuesta es... SI :8ball:",
                                                                  "La respuesta es... NO :8ball:",
                                                                  "Si hubiese un antes despues del mañana del pasado futuristico del presente del mismo momento, ¿Que seguiria despues? :8ball:",
                                                                  "ZZzzzzz... :8ball:",
                                                                  "Si me preguntas que @L e w d e o n#6969 es gay, la respuesta es SI :8ball:",
                                                                  "Si me preguntas que @L e w d e o n#6969 es gay, la respuesta es NO :8ball:",
                                                                  "Las rosas son rojas, el viento las mueve, yo sere el 6 y tu el 9 :heart: :8ball:",
                                                                  "La respuesta es SI, PD: !8riotball es una copia de mi :8ball:",
                                                                  "La respuesta es NO, PD: !8riotball es una copia de mi :8ball:",
                                                                  "La respuesta es un... Kappa :8ball:",
                                                                  "Si el de arriba dice la verdad pero el de abajo miente, ¿Quien tiene la razon? :thinking: :8ball:",
                                                                  "1, 2, 3, 4, 5, 6, 7... CUENTA CONMIGO! :smile: :8ball:",
                                                                  "40%/60% :8ball:",
                                                                  "0%/0% :8ball:",
                                                                  "35%/65% .8ball:",
                                                                  "No te dire la respuesta por que me caes mal! :8ball:",
                                                                  "¿Te has preguntado si existe una pregunta sin respuesta?, Oh ESPERA, que si existe y es la que me acabas de decir! :8ball:",
                                                                  "Si usted me hackeara, conseguira la respuesta! :8ball:",
                                                                  "CLARO QUE SI! :8ball:",
                                                                  "CLARO QUE NO! :8ball:",
                                                                  "Juan clavo un clavo en la calva de un calvito... :8ball:",
                                                                  "Flareon es... ah perdon, la respuesta es SI :8ball:",
                                                                  "Flareon es... ah perdon, la respuesta es NO :8ball:",
                                                                  "**jalandose el ganzo** :8ball:",
                                                                  "Mejor suscribete a mi canal! :8ball:",
                                                                  "Si solo hubiese un mañana... ¿Que harias? :8ball:",
                                                                  "Gracias por perder tu tiempo conmigo! :smile: :8ball:"]))

    elif message.content.startswith("!random number"):
        await client.send_message(message.channel, random.choice(["1 :game_die:",
                                                                  "2 :game_die:",
                                                                  "3 :game_die:",
                                                                  "4 :game_die:",
                                                                  "5 :game_die:",
                                                                  "6 :game_die:",
                                                                  "7 :game_die:",
                                                                  "8 :game_die:",
                                                                  "9 :game_die:",
                                                                  "10 :game_die:",
                                                                  "11 :game_die:",
                                                                  "12 :game_die:",
                                                                  "13 :game_die:",
                                                                  "14 :game_die:",
                                                                  "15 :game_die:",
                                                                  "16 :game_die:",
                                                                  "17 :game_die:",
                                                                  "18 :game_die:",
                                                                  "19 :game_die:",
                                                                  "20 :game_die:",
                                                                  "21 :game_die:",
                                                                  "22 :game_die:",
                                                                  "23 :game_die:",
                                                                  "24 :game_die:",
                                                                  "25 :game_die:",
                                                                  "26 :game_die:",
                                                                  "27 :game_die:",
                                                                  "28 :game_die:",
                                                                  "29 :game_die:",
                                                                  "30 :game_die:",
                                                                  "0 :game_die:",
                                                                  "Mala suerte para ti, Ningun Numero para ti! :joy:",
                                                                  "HAS ENCONTRADO UN NUMERO ESPECIAL :tada: (**6**) :tada: JUNTA TODOS LOS NUMEROS Y xXFireBlastXx Te premiara! :gift:",
                                                                  "HAS ENCONTRADO UN NUMERO ESPECIAL :tada: (**9**) :tada: JUNTA TODOS LOS NUMEROS Y xXFireBlastXx Te premiara! :gift:",
                                                                  "HAS ENCONTRADO UN NUMERO ESPECIAL :tada: (**1**) :tada: JUNTA TODOS LOS NUMEROS Y xXFireBlastXx Te premiara! :gift:",
                                                                  "HAS ENCONTRADO UN NUMERO ESPECIAL :tada: (**9**) :tada: JUNTA TODOS LOS NUMEROS Y xXFireBlastXx Te premiara! :gift:",
                                                                  "HAS ENCONTRADO UN NUMERO ESPECIAL :tada: (**2**) :tada: JUNTA TODOS LOS NUMEROS Y xXFireBlastXx Te premiara! :gift:",
                                                                  "HAS ENCONTRADO UN NUMERO ESPECIAL :tada: (**0**) :tada: JUNTA TODOS LOS NUMEROS Y xXFireBlastXx Te premiara! :gift:",
                                                                  "HAS ENCONTRADO UN NUMERO ESPECIAL :tada: (**0**) :tada: JUNTA TODOS LOS NUMEROS Y xXFireBlastXx Te premiara! :gift:",
                                                                  "HAS ENCONTRADO UN NUMERO ESPECIAL :tada: (**0**) :tada: JUNTA TODOS LOS NUMEROS Y xXFireBlastXx Te premiara! :gift:",
                                                                  "HAS ENCONTRADO UN NUMERO ESPECIAL :tada: (**0**) :tada: JUNTA TODOS LOS NUMEROS Y xXFireBlastXx Te premiara! :gift:",
                                                                  "HAS ENCONTRADO UN NUMERO ESPECIAL :tada: (**5**) :tada: JUNTA TODOS LOS NUMEROS Y xXFireBlastXx Te premiara! :gift:"]))

    elif message.content.startswith("!porn"):
        await client.send_message(message.channel, random.choice(["https://brasilhentai.com/BH/wp-content/uploads/2017/12/Dragon-ball-z-hentai-15.jpg",
                                                                  "https://www.google.com.mx/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjR2JS2i7ncAhUBWa0KHd8GD2oQjRx6BAgBEAU&url=https%3A%2F%2Fwww.pornhub.com%2Fview_video.php%3Fviewkey%3Dph57be736235a11&psig=AOvVaw1fQcQhId2qu5Ab55wZEwVE&ust=1532568083796096",
                                                                  "http://hentaigo.com/wp-content/uploads/thumbs/custom/P/pokemon_moon_hentai_sex.jpg",
                                                                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7UtqDQ6PagP-SY6pUQ6SBZiSdRURTOKyzpW7HpaJIKMgWRBtDEg",
                                                                  "https://i.pinimg.com/600x315/e8/a6/e8/e8a6e8365fc9ace93ab87d2e35690a0e.jpg",
                                                                  "https://www.google.com.mx/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjfvK2ojLncAhUKUK0KHYIYCFwQjRx6BAgBEAU&url=http%3A%2F%2Fwww.lolhentai.net%2Fpicture%3F%2F36388-lusciousnet_lusciousnet_lol_hentai_2k15_wwwcrusangnet_610_1335455482640x0%2Fcategory%2Friven&psig=AOvVaw1fQcQhId2qu5Ab55wZEwVE&ust=1532568083796096",
                                                                  "https://www.google.com.mx/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwib9aaujLncAhVhmK0KHZFdC40QjRx6BAgBEAU&url=https%3A%2F%2Fdanbooru.donmai.us%2Fposts%2F230291&psig=AOvVaw1fQcQhId2qu5Ab55wZEwVE&ust=1532568083796096",
                                                                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWILiC_vZj-pv4dZqv_8kyld5uQ7Ht6a-f0OxRYpRRHsZKEf5i",
                                                                  "https://cdnio.luscious.net/I_am_no_Genius/738/lusciousnet_lusciousnet_lusciousnet_d3_729222691_859157234.jpg",
                                                                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_IrGKcGPevJfCqqAF-XksmUfE68gwDz0DBMUMgM-L3SxdGHfM",
                                                                  "http://drop-books.com/wp-content/uploads/2015/07/00217.jpg",
                                                                  "https://www.google.com.mx/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwinzJvZjLncAhUSUa0KHbw0Bj4QjRx6BAgBEAU&url=https%3A%2F%2Fwww.pornhub.com%2Fview_video.php%3Fviewkey%3Dph5a6bfade479b0&psig=AOvVaw1fQcQhId2qu5Ab55wZEwVE&ust=1532568083796096",
                                                                  "https://megahentai2017.files.wordpress.com/2017/11/84kmeg00019jp-18.jpg?w=800&h=450&crop=1",
                                                                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3IMt2TSWyRqGMcqcdfHCEh37vbu1QEVMKjeR4JbFxLOy1dALp1g",
                                                                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUgKdSsLd7nnSdL5B-anZ4H3BKFd6Hpu-YJWDyxERtZnmZUXAx",
                                                                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSM_0mym8uzk4-W_0XABCF4Z3N_Z76yRpVxZfHJNmnWdWTG9N6i",
                                                                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQK29FNWSlVJJP5p-Kt8rdG9oKBrX_GPBb7L99XnAIw4y4zwuRS",
                                                                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNTUl4_ab2z3KzypcRSSeA5mOyHQU-u-ucfaYNyHGhpRkURRpn",
                                                                  "https://78.media.tumblr.com/9ff4662aceb6cbf024c641ee54bcd42c/tumblr_nsorccYm881uacepyo1_500.gif",
                                                                  "https://www.google.com.mx/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjVw-qgjbncAhUmgK0KHWwcDPEQjRx6BAgBEAU&url=http%3A%2F%2Fwww.hardhentaiporn.com%2F&psig=AOvVaw1fQcQhId2qu5Ab55wZEwVE&ust=1532568083796096",
                                                                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwk88cdFySmNQaj72d7D6WFQsRNFWqA1mtGDoN5KZyJYLpU9tMJQ",
                                                                  "http://www.animetric.com/review_images/3435_princess%20lover!%20ova%20(3).jpg",
                                                                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR__6qC-DCqAB6m5_PJRIm_9rbab2buUXMdgey10Au6JXKKJ3JB",
                                                                  "http://hentaihaven.org/package/2017/09/HH-Boku-Dake-no-Hentai-Kanojo-Motto-The-Animation-Episode-1-DVD-AD82E088.mp4_snapshot_05.41_2017.09.15_20.58.56.png",
                                                                  "data:image/jpeg;base64,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",
                                                                  "https://78.media.tumblr.com/3df8212a75df1ff4fbb7e0ea005f88a8/tumblr_nbttz1muPe1toy0ydo1_400.gif",
                                                                  "https://78.media.tumblr.com/e36b8e40ba4c1d80f3c326dc04a27577/tumblr_oqp1y4SP7g1vkeuowo1_1280.gif",
                                                                  "https://www.google.com.mx/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjc18GyjrncAhUNna0KHViUBBsQjRx6BAgBEAU&url=https%3A%2F%2Fluscious.net%2Fpictures%2Falbum%2Ffire-emblem-arkaneia-aera-fe_77505%2Fid%2F3977818%2F%40_531752_chiki_crossover_fire&psig=AOvVaw3v2r9hcAYVPUiZ-o4rRt8j&ust=1532568811627168",
                                                                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOPKoD215A2Z7_7vbFws11f3BhGlRGQHB0y4i3L6S-4EQHA2O_",
                                                                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5Z1cPEYVvTZ18k36H66o8JCyJlkDH9xofipUroZZs1Ou9ktuX",
                                                                  "https://static.hentai-gifs.com/upload/20160703/19/36972/1.gif",
                                                                  "https://static.hentai-gifs.com/upload/20160630/19/36922/1.gif",
                                                                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSc4UpBa31eA58pCuPmD0f3xbQebAZB33ot5BiFXX5LH6fTj0t2",
                                                                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTU9av0ZCNKEreN6sUfFMiubo7puyhJMe5CGDnhuI8GVlR__eV",
                                                                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCcH7mQIGp7Rv8CGa3HU-Ws48hOQQ-eMCEGtVwWJ544uNW9j1u",
                                                                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQn9_UFa-MNcki8aXvrZ-r8A2t7KMozZPzPVnu97AQ6MZ5eTfl5",
                                                                  "https://78.media.tumblr.com/d11fec9ff8a6d9bfa4f874e779d681c0/tumblr_mqxih2Txqv1sqyex5o1_640.gif",
                                                                  "https://78.media.tumblr.com/931125762652e49075f26f954049c0da/tumblr_msvseafYc01sflbiso1_1280.gif",
                                                                  "https://i.pinimg.com/originals/c3/bf/30/c3bf30419e6a6795b7566bccd418a091.gif",
                                                                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvmgXhjIYGYGD945k_9U8IbYtISemumqGZDncqExoWyd3mHUwt",
                                                                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJ5BPVu2FtXyQ1lQyJas0anJ6wnNsqNo3t6aIzfQ4Jbb2js0A2",
                                                                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-Xc_hVBioVmheVsm5LTJaT898PaJfnNDgyC9zKVuduP6SpSnJ",
                                                                  "http://blog-imgs-48.fc2.com/r/o/r/rorizip8/1323951829848.gif",
                                                                  "https://static.hentai-image.com/upload/20141216/1/216/27.gif",
                                                                  "https://images.sex.com/images/pinporn/2017/04/11/620/17612376.gif",
                                                                  "https://static.hentai-gifs.com/upload/20160506/13/26185/1.gif",
                                                                  "https://78.media.tumblr.com/83a2229a365b3dc42c86dc8e45270529/tumblr_mra0bm24hZ1se7fwao1_1280.gif",
                                                                  "https://simg3.gelbooru.com//images/ba/b0/bab0789b4457d8c1789db276689e137b.gif",
                                                                  "http://24.media.tumblr.com/08d86921bbaf98a9dc761ce1f21842f1/tumblr_n40jd7qxVe1sjyos5o1_500.gif",
                                                                  "https://raikou1.donmai.us/3b/08/__poko_poko_gunshou_2__3b082ece1c517f8fcad26f55fe6227b6.gif"]))

    elif message.content.startswith("!random text"):
        await client.send_message(message.channel, random.choice(["Eres hermoso!",
                                                                  "Casate CONMIGO",
                                                                  "Te odio!",
                                                                  "Nadie te quiere!",
                                                                  "Matate!",
                                                                  "Te amo!",
                                                                  "¿Quien eres?",
                                                                  "Hola",
                                                                  "No me hagas caso, solo soy un bot",
                                                                  "Flareon is a woman",
                                                                  "xXFireBlastXx is a men",
                                                                  "Flareon GDPS esta muriendo",
                                                                  "Mejor usa !porn",
                                                                  "Mejor usa !random number",
                                                                  "Mejor usa !8ball",
                                                                  "RuhGi es un inactivo"]))
    elif message.content.startswith("!firehelp"):
        await client.send_message(message.channel, random.choice(["**!8ball** Responde tus preguntas, **!random number** Genera un numero aleatorio, **!porn** Genera una imagen XXX, **!deposite (numero) (pregunta)** Deposita un numero de monedas para desbloquear una respuesta!"]))
                                  
                               
client.run("your token here")
                                  
