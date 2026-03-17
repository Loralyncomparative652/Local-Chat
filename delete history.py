if input('Are you sure? [y/n]\nВы уверены? [д/н]\n> ').lower() in ['д', 'y', 'да', 'yes']:
    with open('History_b.json', 'w') as f: f.close()
    with open('History_c.json', 'w') as f: f.close()