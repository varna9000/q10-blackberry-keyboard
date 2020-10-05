from machine import Pin, Timer
import utime

colsPins=[26,27,14,12,13]
rowsPins=[25,33,32,15,5,19,4]
cols=[0,0,0,0,0]
rows=[0,0,0,0,0,0,0]


SYM=0
ALT=0
SHIFT=0
SOUND=0
MIC=0


letters=[
    ['q', 'e', 'r', 'u', 'o'],
    ['w', 's', 'g', 'h', 'l'],
    [SYM, 'd', 't', 'y', 'i'],
    ['a', 'p', SHIFT, '\n', '\b \b'],
    [ALT, 'x', 'v', 'b', '$'],
    [' ', 'z', 'c', 'n', 'm'],
    [MIC, SHIFT, 'f', 'j', 'k']
]

cyr_letters=[
    ['я', 'е', 'р', 'у', 'о'],
    ['в', 'с', 'г', 'х', 'л'],
    [SYM, 'д', 'т', 'ъ', 'и'],
    ['а', 'п', 'ю', '\n', '\b \b'],
    [ALT, 'ь', 'ж', 'б', 'ш'],
    [' ', 'з', 'ц', 'н', 'м'],
    ['ч', 'щ', 'ф', 'й', 'к']
]

symbols=[
    ['#', '2', '3', '_', '+'],
    ['1', '4', '/', ':', '"'],
    [SYM, '5', '(', ')', '-'],
    ['*', '@', SHIFT , '\n', '\b \b'],
    [ALT, '8', '?', '!', SOUND],
    [' ', '7', '9', ',', '.'],
    ['0', SHIFT, '6', ';', '`']
]

#def on_pressed(timer):
#    global debounced
#    row=debounced

#def callback(p):
#    global row
#    p.irq(trigger=0)
#    row=p
#    global pressed
#    pressed = 1
    #timer.init(mode=Timer.ONE_SHOT, period=200, callback=on_pressed)
    #p.irq(trigger=0)
#timer = Timer(0)


def debounce(pin):
    # wait for pin to change value
    # it needs to be stable for a continuous 20ms
    cur_value = pin.value()
    active = 0
    while active < 20:
        if pin.value() != cur_value:
            active += 1
        else:
            active = 0
        utime.sleep_ms(1)


for i in range(len(cols)):
    cols[i]=Pin(colsPins[i],Pin.OUT)
    cols[i].value(0)
    #print("col{}:{}".format(i,cols[i]))
    
    
for i in range(len(rows)):
    rows[i]=Pin(rowsPins[i],Pin.IN, Pin.PULL_UP)
    rows[i].value(1)
    #rows[i].irq(trigger=Pin.IRQ_FALLING, handler=callback)
    #print("row{}:{}".format(i,rows[i]))

while True:
    
    if SYM:
        keys=symbols
    elif ALT:
        keys=cyr_letters
    else:
        keys=letters
        
    cols[0].value(0)
    for z in range(len(rows)):
        if rows[z].value()==0:
            debounce(rows[z])
            if z==4:
                ALT =~ALT
            elif z==2:
                SYM =~SYM
            else:    
                #print("row:{}, col:{}".format(rows[z],cols[0]))
                ch=keys[z][0]
                if SHIFT:
                    ch=ch.upper()
                
                print(ch,end='')
                          
    cols[0].value(1)
    
    cols[1].value(0)
    for z in range(len(rows)):
        if rows[z].value()==0:
            debounce(rows[z])
            #print("row:{}, col:{}".format(rows[z],cols[1]))
            if z==6 and ALT==0:
                SHIFT=~SHIFT
            else:    
                ch=keys[z][1]
                if SHIFT:
                    ch=ch.upper()
                print(ch,end='')
                          
    cols[1].value(1)
    
    cols[2].value(0)
    for z in range(len(rows)):
        if rows[z].value()==0:
            debounce(rows[z])
            if z==3 and ALT==0:
                SHIFT=~SHIFT
            else:    
            #print("row:{}, col:{}".format(rows[z],cols[2]))
                ch=keys[z][2]
                if SHIFT:
                    ch=ch.upper()
                print(ch,end='')
                          
    cols[2].value(1)
    
    cols[3].value(0)
    for z in range(len(rows)):
        if rows[z].value()==0:
            debounce(rows[z])
            #print("row:{}, col:{}".format(rows[z],cols[3]))
            ch=keys[z][3]
            if SHIFT:
                ch=ch.upper()
            print(ch,end='')
                          
    cols[3].value(1)
    
    cols[4].value(0)
    for z in range(len(rows)):
        if rows[z].value()==0:
            debounce(rows[z])
            #print("row:{}, col:{}".format(rows[z],cols[4]))
            ch=keys[z][4]
            if SHIFT:
                ch=ch.upper()
            print(ch,end='')
                          
    cols[4].value(1)      