def minimax(node, depth, isMaximizingPlayer, alpha, beta, stop_con_func=None):
    """
    node: the current node that keep the game state
    depth: depth of the tree 
    isMaximizingPlayer: True if this is the turn of the player you want to maximize the score and vice versa
    alpha: the best value of the maximizer can guarantee at the above level
    beta:  the best value of the minimizer can guarantee at the above level
    stop_con_func: the stop condition function that terminated the algo, default None
    """
    if node.is_leaf_node():
        return node.val

    if isMaximizingPlayer:
        best_val = float('-inf')
        for child in node.children():
            value = minimax(node, depth+1, False, alpha, beta)
            best_val = max(value, best_val)
            alpha = max(alpha, best_val)
            if beta <= alpha:
                break;
        return best_val
    
    else:
        best_val= float('inf')
        for child in node.children():
            value = minimax(node, depth+1, True, alpha, beta)
            best_val = min(value, best_val)
            beta  = min(beta, best_val)
            if beta <= alpha:
                break;
        return best_val
