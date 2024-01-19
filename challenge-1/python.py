def allocate_subnets(nat_instances, subnets):
    nat_instances.sort(key=lambda x: len(x['subnets']))

    for subnet in subnets:
        allocated = False

        # Try to allocate to the same AZ first
        for nat_instance in nat_instances:
            if nat_instance['az'] == subnet['az'] and \
                    nat_instance['weight'] + subnet['weight'] <= sum(subnet['weight'] for subnet in subnets) / len(nat_instances):
                nat_instance['subnets'].append(subnet['id'])
                nat_instance['weight'] += subnet['weight']
                allocated = True
                break

        # If no NATInstance in the same AZ or weight constraint is not met, allocate to any other available NATInstance
        if not allocated:
            for nat_instance in nat_instances:
                if nat_instance['weight'] + subnet['weight'] <= sum(subnet['weight'] for subnet in subnets) / len(nat_instances):
                    nat_instance['subnets'].append(subnet['id'])
                    nat_instance['weight'] += subnet['weight']
                    break

    # Print the result
    for nat_instance in nat_instances:
        print(f"Instance ({nat_instance['id']} - {nat_instance['az']}):")
        for subnet_id in nat_instance['subnets']:
            print(f" subnet ({subnet_id} - {subnets[subnet_id-1]['az']})")


nat_instances = [
    {'id': 1, 'az': 'us-west1-a', 'subnets': [], 'weight': 0},
    {'id': 2, 'az': 'us-west1-b', 'subnets': [], 'weight': 0},
    {'id': 3, 'az': 'us-west1-c', 'subnets': [], 'weight': 0},
]

subnets = [
    {'id': 1, 'az': 'us-west1-a', 'weight': 1},
    {'id': 2, 'az': 'us-west1-b', 'weight': 2},
    {'id': 3, 'az': 'us-west1-b', 'weight': 3},
    {'id': 4, 'az': 'us-west1-c', 'weight': 4},
]

allocate_subnets(nat_instances, subnets)
