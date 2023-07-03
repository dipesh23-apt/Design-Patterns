from pizza import Pizza,Cheese,Mushroom,Olives

def main():
    margherita=Pizza('Margherita',10)
    margherita_with_cheese=Cheese(margherita)
    print(margherita_with_cheese.get_cost())
    margherita_with_cheese_and_mushroom=Mushroom(margherita_with_cheese)
    margherita_with_cheese_mushroom_olives=Olives(margherita_with_cheese_and_mushroom)

    total_cost=margherita_with_cheese_mushroom_olives.get_cost()
    print('---------------------------------')
    print('Order Details')
    print('---------------------------------')
    print('Pizza: ',margherita_with_cheese_mushroom_olives.get_description())
    print('Total Cost: ',total_cost)

if __name__=='__main__':
    main()