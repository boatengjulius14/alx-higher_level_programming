#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	fast = list;
	slow = list;

	if (!list)
		return (0);
	
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
