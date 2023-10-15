#include "lists.h"
/**
 * check_cycle - checks if a linked list contains a cycle
 *               using Floyd's Tortoise and Hare algorithm
 * where a pointer moves by one step and other moves by two
 * if there is a cycle after some iterations the fast pointer
 * will be at the same position of the slow
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
listint_t *slow = list;
listint_t *fast = list;

if (!list)
return (0);

while (slow && fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
return (1);
}
return (0);
}
