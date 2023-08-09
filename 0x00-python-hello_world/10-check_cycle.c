#include "lists.h"

/**
 * check_cycle - this function checks if a linked list
 * contains a cycle
 * @list: this is a pointer to the list
 *
 * Return: on success 1, else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list; /* first cycle to look through */
	listint_t *second = list; /* second cycle to look through */

	if (list == NULL)
	{
		return (0);
	}
	while (first && second && second->next)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
		{
			return (1);
		}
	}
	return (0);
}
